from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Hotel)
admin.site.register(models.Service)
admin.site.register(models.Guest)
admin.site.register(models.GuestAddress)