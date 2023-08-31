from .models import Hotel, Service
from rest_framework import serializers

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class ServiceSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"