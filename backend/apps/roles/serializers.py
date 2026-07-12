from rest_framework import serializers
from .models import RestaurantOwner, Rider

class RestaurantApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantOwner
        fields = [
            "id",
            "business_name",
            "pan_number",
            "citizenship_front",
            "citizenship_back",
            "verification_status",
        ]

        read_only_fields = ["id", "verification_status"]

    def create(self, validated_data):
        user = self.context["request"].user

        if hasattr(user, "restaurant_profile"):
            raise serializers.ValidationError(
                "You have already applied as a restaurant owner."
            )

        return RestaurantOwner.objects.create(user=user, **validated_data)


class RiderApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = [
            "id",
            "vehicle",
            "license_number",
            "license_image",
            "verification_status",
        ]

        read_only_fields = ["id", "verification_status"]

    def create(self, validated_data):
        user = self.context["request"].user

        if hasattr(user, "rider_profile"):
            raise serializers.ValidationError(
                "You have already applied as a rider."
            )

        return Rider.objects.create(user=user, **validated_data)