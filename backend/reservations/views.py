from rest_framework import viewsets, permissions, status
from .serializers import ReservationSerializer
from .models import Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]



