from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import RestaurantOwner, Rider
from .serializers import (
    RestaurantApplicationSerializer,
    RiderApplicationSerializer,
    RestaurantApprovalSerializer,
    RiderApprovalSerializer,
)


# Restaurant
class RestaurantApplicationView(generics.CreateAPIView):
    serializer_class = RestaurantApplicationSerializer
    permission_classes = [IsAuthenticated]


class MyRestaurantProfileView(generics.RetrieveAPIView):
    serializer_class = RestaurantApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.restaurant_profile


class RestaurantStatusUpdateView(generics.UpdateAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantApprovalSerializer
    permission_classes = [IsAdminUser]


# Rider
class RiderApplicationView(generics.CreateAPIView):
    serializer_class = RiderApplicationSerializer
    permission_classes = [IsAuthenticated]


class MyRiderProfileView(generics.RetrieveAPIView):
    serializer_class = RiderApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.rider_profile


class RiderStatusUpdateView(generics.UpdateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderApprovalSerializer
    permission_classes = [IsAdminUser]