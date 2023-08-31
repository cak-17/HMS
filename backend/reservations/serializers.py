from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'confirmation_code',
            'check_in', 
            'check_out', 
            'status',
            'guest',
            'room'
        ]
