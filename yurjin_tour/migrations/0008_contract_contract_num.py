# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-26 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0007_auto_20161026_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]