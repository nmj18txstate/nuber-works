# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied'), ('offline', 'Offline')], max_length=100),
        ),
    ]
