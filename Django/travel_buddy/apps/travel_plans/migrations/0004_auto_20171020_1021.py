# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0003_trips_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='trips2', to='travel_plans.Users')),
            ],
        ),
        migrations.DeleteModel(
            name='Trips',
        ),
    ]