# inventory/urls.py
from django.urls import path

from .views import api_create_inventory_item, api_inventory_list

urlpatterns = [
    path('inventories', api_inventory_list, name='api_inventory_list'),
    path('inventories/create', api_create_inventory_item, name='api_create_inventory_item'),
]
