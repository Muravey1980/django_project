# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0017_auto_20161114_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_type_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание'),
        ),
    ]
