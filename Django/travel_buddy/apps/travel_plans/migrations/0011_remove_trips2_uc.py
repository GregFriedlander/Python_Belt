# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0010_trips2_uc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips2',
            name='uc',
        ),
    ]