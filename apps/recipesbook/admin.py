from django.contrib import admin

from .models import Recipe, Ingredient, Amount

admin.site.register(Amount)
admin.site.register(Ingredient)
admin.site.register(Recipe) 
# Register your models here.
