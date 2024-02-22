from django.contrib import admin
from .models import *


class IngredientsInline(admin.TabularInline):
    fk_name = 'recipe'
    model = Ingredients
    extra = 5


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline]


class InstructionInline(admin.TabularInline):
    fk_name = 'instruction'
    model = Instruction
    extra = 5


class InstructionAdmin(admin.ModelAdmin):
    inlines = [InstructionInline]


admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Difficulty)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Instruction)
admin.site.register(Ingredients)
admin.site.register(CarouselImage)

# Register your models here.
