# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0037_auto_20161118_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourist',
            name='full_name_r',
            field=models.CharField(blank=True, max_length=200, verbose_name='ФИО в родительном падеже'),
        ),
    ]
