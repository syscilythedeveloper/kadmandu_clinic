# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
