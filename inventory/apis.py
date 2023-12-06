# inventory/urls.py
from django.urls import path

from .views import api_inventory_list

urlpatterns = [
    path('/inventories', api_inventory_list, name='api_inventory_list'),
]
