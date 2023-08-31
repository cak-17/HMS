from django.db.models import Q

from .models import Reservation
from rooms.models import Room

def get_availability_by_category(room_category_slug, check_in, check_out, num_of_guests=1):
    conflicting_reservations = Reservation.objects.filter(
        Q(status=2) | Q(status=1),
        room__category__slug=room_category_slug,
        check_out__gt=check_in,
        check_in__lt=check_out,
        #room__category__capacity__lt=num_of_guests,
    )
    print(conflicting_reservations)
    print(conflicting_reservations.filter(room__status=Room.RoomStatus.OOO))
    booked_rooms_id = conflicting_reservations.values('room_id')
    print(booked_rooms_id)
    available_rooms = Room.objects.filter(category__slug=room_category_slug).exclude(id__in=booked_rooms_id)
    print(available_rooms)
    return available_rooms