# Generated by Django 4.2.4 on 2023-08-24 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='SNG', help_text='3 digits ID for Room Categories', max_length=3, verbose_name='Category ID')),
                ('name', models.CharField(default='SINGLE', max_length=50)),
                ('description', models.TextField(blank=True, help_text='Max 500 characters, HTML included', max_length=500, null=True)),
                ('beds', models.PositiveSmallIntegerField(default=1)),
                ('capacity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.FloatField(default=100.0)),
                ('services', models.ManyToManyField(to='core.service')),
            ],
            options={
                'verbose_name': 'Room Category',
                'verbose_name_plural': 'Room Categories',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomcategory')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]