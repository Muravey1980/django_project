# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-10 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0051_auto_20170310_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='signatory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_signatory', to='yurjin_tour.Manager', verbose_name='Подписант'),
        ),
    ]