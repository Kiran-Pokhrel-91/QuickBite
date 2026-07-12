from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import RestaurantOwner, Rider
from .serializers import RestaurantApplicationSerializer, RiderApplicationSerializer


class RestaurantApplicationView(generics.CreateAPIView):
    serializer_class = RestaurantApplicationSerializer
    permission_classes = [IsAuthenticated]


class RiderApplicationView(generics.CreateAPIView):
    serializer_class = RiderApplicationSerializer
    permission_classes = [IsAuthenticated]


class MyRestaurantProfileView(generics.RetrieveAPIView):
    serializer_class = RestaurantApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.restaurant_profile


class MyRiderProfileView(generics.RetrieveAPIView):
    serializer_class = RiderApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.rider_profile
    
