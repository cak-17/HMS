from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookingSerializer
from .models import Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

