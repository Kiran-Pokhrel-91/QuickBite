from django.urls import path

from .views import (
    RestaurantApplicationView,
    MyRestaurantProfileView,
    RestaurantStatusUpdateView,

    RiderApplicationView,
    MyRiderProfileView,
    RiderStatusUpdateView,
)

urlpatterns = [
    # Restaurant
    path("restaurant/apply/", RestaurantApplicationView.as_view(), name="restaurant-apply"),
    path("restaurant/me/", MyRestaurantProfileView.as_view(), name="restaurant-profile"),
    path("restaurant/<uuid:pk>/status/", RestaurantStatusUpdateView.as_view(), name="restaurant-status"),

    # Rider
    path("rider/apply/", RiderApplicationView.as_view(), name="rider-apply"),
    path("rider/me/", MyRiderProfileView.as_view(), name="rider-profile"),
    path("rider/<uuid:pk>/status/", RiderStatusUpdateView.as_view(), name="rider-status"),
]