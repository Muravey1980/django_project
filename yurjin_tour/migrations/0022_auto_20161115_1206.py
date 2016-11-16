# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0021_auto_20161115_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='input_date',
        ),
        migrations.AddField(
            model_name='contract',
            name='doc_get_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата получения документов клиентом'),
        ),
    ]
