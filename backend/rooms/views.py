from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RoomSerializer, RoomCategorySerializer
from .models import Room, RoomCategory


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomCategoryViewSet(viewsets.ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

