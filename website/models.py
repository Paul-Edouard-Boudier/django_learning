from django.db import models
from datetime import datetime


class IngredientType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CannedFoodType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    We do not want to delete the Type object when an ingredient disappears
    However, we might want to delete the CannedFood associated with it
    """
    name = models.CharField(max_length=20)
    type = models.ForeignKey(IngredientType, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class CannedFood(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.IntegerField(default=1)
    note = models.TextField(max_length=1000)
    type = models.ForeignKey(CannedFoodType, on_delete=models.PROTECT)
    limited_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return [i for i in self.ingredients.all()]

    def get_stocks(self):
        return [s for s in self.stock_set.all()]


class Stock(models.Model):
    weight = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    cannedfood = models.ForeignKey(CannedFood, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cannedfood.name}_{self.weight}g'


class Order(models.Model):
    order_number = models.IntegerField(default=0)
    canned_food = models.ManyToManyField(CannedFood)
    delivery_number = models.CharField(max_length=100)

    def __str__(self):
        return self.order_number
