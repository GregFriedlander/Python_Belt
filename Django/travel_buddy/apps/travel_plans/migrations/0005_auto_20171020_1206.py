# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0004_auto_20171020_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips2',
            name='users',
            field=models.ManyToManyField(related_name='trips', to='travel_plans.Users'),
        ),
    ]
