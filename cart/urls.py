from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail, name='cart'),
    path('add_to_cart/<int:stock_id>', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:stock_id>', views.delete_from_cart, name='delete_from_cart'),
]
