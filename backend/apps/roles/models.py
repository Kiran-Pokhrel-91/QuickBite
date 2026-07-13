from django.db import models
from apps.users.models import User
from apps.users.models import BaseModel

# Create your models here.

class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    
    def __str__(self):
        return self.user.email
    
class RestaurantOwner(BaseModel):
    class VerificationStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant_profile')

    business_name = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=50)
    citizenship_front = models.ImageField(upload_to="kyc/restaurant/front/")
    citizenship_back = models.ImageField(upload_to="kyc/restaurant/back/")

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING
    )

    def __str__(self):
        return self.business_name


class Rider(BaseModel):
    class VerificationStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    class Vehicle(models.TextChoices):
        BIKE = "BIKE", "Bike"
        SCOOTER = "SCOOTER", "Scooter"
        BICYCLE = "BICYCLE", "Bicycle"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rider_profile")
    vehicle = models.CharField(max_length=20, choices=Vehicle.choices)

    license_number = models.CharField(max_length=100)
    license_image = models.ImageField(upload_to="kyc/rider/license/")

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING
    )
    
    def __str__(self):
        return self.user.email