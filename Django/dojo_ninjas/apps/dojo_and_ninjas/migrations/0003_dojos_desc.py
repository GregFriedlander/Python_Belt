# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-17 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_and_ninjas', '0002_auto_20171016_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]