# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-02 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0010_auto_20161102_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_sum',
            field=models.IntegerField(default=0, null=True, verbose_name='Сумма контракта'),
        ),
    ]
