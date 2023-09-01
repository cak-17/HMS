from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import RoomSerializer, RoomCategorySerializer
from .models import Room, RoomCategory
from .utils import get_availability_by_category


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomCategoryViewSet(viewsets.ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def check_avail(request, format=None):
    if request.method == 'POST':
        rooms = get_availability_by_category(
            room_category_slug=request.data['room_category_slug'],
            check_in=request.data['check_in'],
            check_out=request.data['check_out'],
            num_of_guests=1
        )
        if len(rooms) > 0:
            return Response(RoomSerializer(rooms, context={"request":request}, many=True).data)
        return Response({"message": "Room Not Found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)