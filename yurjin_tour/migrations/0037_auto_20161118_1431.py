# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0036_auto_20161118_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touragency',
            old_name='country_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tourist',
            old_name='tourist_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='tourist',
            old_name='tourist_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='tourist',
            old_name='tourist_mid_name',
            new_name='mid_name',
        ),
    ]
