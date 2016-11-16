# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0025_auto_20161116_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='tour_orepator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='yurjin_tour.TourOperator', verbose_name='Туроператор'),
        ),
    ]
