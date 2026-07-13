from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User

# create your models here.
class Restaurant(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)

    is_active = models.BooleanField(default=True, db_index=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['owner', 'is_active']),
        ]
        ordering = ['-id']