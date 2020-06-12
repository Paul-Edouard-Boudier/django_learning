from django.contrib import admin
from website.models import CannedFood, Ingredient, IngredientType, CannedFoodType, Stock, Order

admin.site.register(CannedFood)
admin.site.register(Ingredient)
admin.site.register(IngredientType)
admin.site.register(CannedFoodType)
admin.site.register(Stock)
admin.site.register(Order)
