# Generated by Django 4.2.4 on 2023-08-24 18:43

import bookings.models
import core.utils.time
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(default=core.utils.time.get_default_checkin)),
                ('check_out', models.DateField(default=core.utils.time.get_default_checkout)),
                ('arrival_time', models.TimeField(default=datetime.time(15, 0))),
                ('notes', models.TextField(blank=True, max_length=400, null=True)),
                ('requested_on', models.DateField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Requested'), (2, 'Confirmed'), (3, 'Cancelled')], default=1)),
                ('confirmation_code', models.CharField(default=bookings.models.generate_unique_code, max_length=8, unique=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
