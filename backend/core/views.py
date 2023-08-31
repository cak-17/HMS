from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HotelSerializer, ServiceSerializer, GuestSerializer
from .models import Hotel, Service, Guest

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [permissions.AllowAny]