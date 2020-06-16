from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail, name='cart'),
    path('add_to_cart/<int:stock_id>', views.add_to_cart, name='add_to_cart')
]
