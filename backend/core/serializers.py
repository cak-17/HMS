from .models import Hotel, Service, Guest
from rest_framework import serializers

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name"]