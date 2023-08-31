from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Service


class RoomCategory(models.Model):
    class Meta:
        verbose_name = _("Room Category")
        verbose_name_plural = _("Room Categories")

    slug = models.SlugField(
        max_length=3,
        default="SNG",
        verbose_name=_("Category ID"),
        help_text=_("3 digits ID for Room Categories"),
    )
    name = models.CharField(max_length=50, default="SINGLE")
    description = models.TextField(
        max_length=500,
        help_text=_("Max 500 characters, HTML included"),
        blank=True,
        null=True
    )
    beds = models.PositiveSmallIntegerField(default=1)
    capacity = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField(default=100.00)
    #image
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

class Room(models.Model):
    class Meta:
        ordering = ["number"]

    number = models.IntegerField(unique=True)
    category = models.ForeignKey(RoomCategory, related_name="category", on_delete=models.CASCADE)

    def __str__(self):
        return _("%(number)s %(name)s with %(beds)s for %(capacity)s people") % {
            "number": self.number,
            "name": self.category.name,
            "beds": self.category.beds,
            "capacity": self.category.capacity
        }

