# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-22 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0044_auto_20161122_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourist',
            old_name='passport',
            new_name='passport_num',
        ),
    ]
