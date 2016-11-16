# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0027_office_office_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='resort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='yurjin_tour.Resort', verbose_name='Курорт'),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
    ]
