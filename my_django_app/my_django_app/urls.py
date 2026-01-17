from django.contrib import admin
from django.urls import path
from aplikasi.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("recipes/", recipes, name="recipes"),
    path("recipe/<int:recipe_id>/", recipe_detail, name="recipe_detail"),
    path("about/", about, name="about"),
    
    # Form Processing Features
    path("submit-recipe/", submit_recipe, name="submit_recipe"),
    path("budget-calculator/", budget_calculator, name="budget_calculator"),
]