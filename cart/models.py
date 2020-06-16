from django.db import models
from datetime import datetime
from django.db.models import Sum, F

from website.models import Stock

"""
Création d'un panier contenant des article (product)
1 article est un stock avec une quantité pour savoir cb on en veux dans le panier

Il faut avoir le total du panier en multipliant le
prix de l'article * la quantité pour chaque article du panier

"""


class Product(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def product_price(self):
        return self.quantity * self.item.cannedfood.price


class Cart(models.Model):
    """
    Can change shipping fees to another model with predefinite fees
    """
    cartitems = models.ManyToManyField(Product)
    ordered_at = models.DateField(default=datetime.now)
    created_at = models.DateField(default=datetime.now)
    shipping_fees = models.IntegerField(default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def cart_price(self):
        queryset = self.cartitems.aggregate(
            total_price=Sum(F('quantity') * F('item__cannedfood__price'))
        )
        return queryset['total_price']

    @property
    def total_items_in_cart(self):
        queryset = self.cartitems.all().aggregate(
            total_items=models.Sum('quantity')
        )
        return queryset['total_items']
