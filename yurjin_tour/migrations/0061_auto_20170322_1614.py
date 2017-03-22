# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0060_remove_contract_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='yurjin_tour.Manager', verbose_name='Договор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default='2017-01-01', verbose_name='Дата внесения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yurjin_tour.Contract', verbose_name='Договор'),
        ),
    ]
