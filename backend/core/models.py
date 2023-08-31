from datetime import time, timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    pref_arrival_time = models.TimeField(
        default=time(15, 00), verbose_name=_("Preferred Arrival Time")
    )
    min_staying_duration = models.DurationField(
        default=timedelta(days=2), verbose_name=_("Minimum Booking Nights")
    )
    max_staying_duration = models.DurationField(
        default=timedelta(days=30), verbose_name=_("Maximum Booking Nights")
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(
        max_length=300, help_text=_("Max 300 characters"), blank=True, null=True
    )
    icon = models.CharField(
        max_length=100,
        help_text=_("Font Awesome class format ex. 'fa-solid fa-check'"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class GuestAddress(models.Model):
    street = models.CharField(max_length=200)
    street_number = models.CharField(max_length=200)
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Guests(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(GuestAddress, on_delete=models.CASCADE)