from django.urls import path

from .views import (
    RestaurantApplicationView,
    RiderApplicationView,
    MyRestaurantProfileView,
    MyRiderProfileView,
)

urlpatterns = [
    path("restaurant/apply/", RestaurantApplicationView.as_view(), name="restaurant-apply"),
    path("restaurant/me/", MyRestaurantProfileView.as_view(), name="restaurant-profile"),
    path("rider/apply/", RiderApplicationView.as_view(), name="rider-apply"),
    path("rider/me/", MyRiderProfileView.as_view(), name="rider-profile"),
]