# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-26 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0002_auto_20161025_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='office_adddress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
