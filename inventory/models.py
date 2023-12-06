# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    expire_date = models.DateField
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    ndc_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
