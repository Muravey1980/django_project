# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-02 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0012_auto_20161102_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='prepayment',
            new_name='prepayment_sum',
        ),
    ]
