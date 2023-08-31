from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HotelSerializer, ServiceSeralizer
from .models import Hotel, Service

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSeralizer
    permission_classes = [permissions.AllowAny]