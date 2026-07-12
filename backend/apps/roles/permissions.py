from rest_framework.permissions import BasePermission


class IsRestaurantOwner(BasePermission):
    message = "You must be a verified restaurant owner."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "restaurant_profile")
            and request.user.restaurant_profile.is_verified
        )


class IsRider(BasePermission):
    message = "You must be a verified rider."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "rider_profile")
            and request.user.rider_profile.is_verified
        )


class IsCustomer(BasePermission):
    message = "You must be a customer."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "customer_profile")
        )