# inventory/views.py
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import InventoryItemForm
from .models import InventoryItem
from .serializers import InventoryItemSerializer


def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

@api_view(['GET'])
def api_inventory_list(request):
    items = InventoryItem.objects.all()
    serializer = InventoryItemSerializer(items, many=True)
    return Response(serializer.data)

def create_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()

    return render(request, 'inventory/create_inventory_item.html', {'form': form})

@api_view(['POST'])
def api_create_inventory_item(request):
    serializer = InventoryItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # 201 Created
    return Response(serializer.errors, status=400) 