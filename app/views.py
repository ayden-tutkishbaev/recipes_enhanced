from django.shortcuts import render
from .models import *


def index(request):
    categories = Category.objects.all()
    cuisines = Cuisine.objects.all()
    difficulties = Difficulty.objects.all()
    recipe = Recipe.objects.all()

    context = {
        'title': 'Главная',
        'categories': categories,
        'cuisines': cuisines,
        'difficulties': difficulties,
        'recipes': recipe
    }

    return render(request, 'recipes/index.html', context)


