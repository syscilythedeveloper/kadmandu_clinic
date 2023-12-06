# inventory/urls.py
from django.urls import path
from .views import inventory_list, create_inventory_item

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('create/', create_inventory_item, name='create_inventory_item'),
]
