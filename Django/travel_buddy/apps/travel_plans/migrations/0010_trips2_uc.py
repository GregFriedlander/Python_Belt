# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0009_remove_trips2_user_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips2',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uc', to='travel_plans.Users'),
            preserve_default=False,
        ),
    ]