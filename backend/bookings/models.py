import random
import datetime
import string
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from rooms.models import Room
from django.conf import settings
from core.utils.time import get_default_checkin, get_default_checkout

def generate_unique_code(length=settings.MAX_UIID_LENGTH):
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if Booking.objects.filter(confirmation_code=code).count() == 0:
            break
    return code

# Create your models here.
class Booking(models.Model):
    class BookingStatus(models.IntegerChoices):
        REQ = 1, "Requested"
        CONF = 2, "Confirmed"
        CANC = 3, "Cancelled"

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(default=get_default_checkin)
    check_out = models.DateField(default=get_default_checkout)
    arrival_time = models.TimeField(default=datetime.time(15, 00))
    notes = models.TextField(max_length=400, blank=True, null=True)
    requested_on = models.DateField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=BookingStatus.choices, default=BookingStatus.REQ
    )
    confirmation_code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True
    )
    guests = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.user} | {self.confirmation_code} | {self.check_in}"

    def get_absolute_url(self):
        return reverse("Booking_detail", kwargs={"pk": self.pk})

    def get_booking_status(self):
        return Booking.BookingStatus(self.status).label
