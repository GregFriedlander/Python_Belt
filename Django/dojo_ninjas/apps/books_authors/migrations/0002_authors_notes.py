# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-17 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
