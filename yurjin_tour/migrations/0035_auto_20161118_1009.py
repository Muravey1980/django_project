# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0034_auto_20161118_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Сумма контракта'),
        ),
    ]