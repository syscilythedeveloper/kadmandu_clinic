# inventory/urls.py
from django.urls import path

from .views import create_inventory_item, inventory_list

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('create/', create_inventory_item, name='create_inventory_item'),
]
