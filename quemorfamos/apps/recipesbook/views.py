from django.shortcuts import render
from .models import Recipe

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_recipe_list = Recipe.objects.order_by('-datetime')[:5]
    output = ', '.join([p.title for p in latest_recipe_list])
    return HttpResponse(output)
