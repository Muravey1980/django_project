# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0028_auto_20161116_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resort',
            old_name='resort_country',
            new_name='country',
        ),
    ]
