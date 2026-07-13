from django.db import models
from apps.resturants.models import Restaurant
from apps.common.models import BaseModel


# Create your models here.
class MenuItem(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    is_available = models.BooleanField(default=True, db_index=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        indexes = [
            models.Index(fields=['restaurant', 'is_available']),
            models.Index(fields=['name']),
        ]