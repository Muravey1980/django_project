# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-21 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0042_auto_20161121_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='touragency',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yurjin_tour.Manager', verbose_name='Директор'),
        ),
    ]