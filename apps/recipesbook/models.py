from django.db import models


class Ingredient(models.Model):
    name = models.CharField(blank=False, max_length=40, unique=True)
    check = models.BooleanField(default=False)
    datetime = models.DateTimeField('date_published')
   
    def __str__(self):
        return self.name


class Recipe(models.Model):
    recipe_text = models.TextField(blank=False)
    title = models.CharField(blank=False, max_length=40)
    datetime = models.DateTimeField('date_published')
    ingredients = models.ManyToManyField(Ingredient, through='Amount')

    def __str__(self):
        return self.title


class Amount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_joined = models.DateField()
    cant = models.FloatField()
# Create your models here.
