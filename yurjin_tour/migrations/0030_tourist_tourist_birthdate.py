# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-17 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0029_auto_20161116_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourist',
            name='tourist_birthdate',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 11, 17, 5, 22, 13, 57511, tzinfo=utc), verbose_name='Дата рождения'),
            preserve_default=False,
        ),
    ]
