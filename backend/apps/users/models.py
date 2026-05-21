from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel

# Create your models here.
class User(BaseModel, AbstractUser):
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_no"]

    def __str__(self):
        return self.username
