from rest_framework.permissions import BasePermission

from .models import RestaurantOwner, Rider


class IsRestaurantOwner(BasePermission):
    message = "You must be an approved restaurant owner."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "restaurant_profile")
            and request.user.restaurant_profile.verification_status == RestaurantOwner.VerificationStatus.APPROVED
        )


class IsRider(BasePermission):
    message = "You must be an approved rider."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "rider_profile")
            and request.user.rider_profile.verification_status == Rider.VerificationStatus.APPROVED
        )


class IsCustomer(BasePermission):
    message = "You must be a customer."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "customer_profile")
        )