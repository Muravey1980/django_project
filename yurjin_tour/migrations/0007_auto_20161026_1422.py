# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-26 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0006_auto_20161026_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='yurjin_tour.Tourist'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='tourist_list',
            field=models.ManyToManyField(related_name='tourist_list', to='yurjin_tour.Tourist'),
        ),
    ]
