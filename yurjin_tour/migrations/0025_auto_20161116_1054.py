# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0024_auto_20161116_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touroperator',
            name='fact_address',
            field=models.CharField(max_length=200, verbose_name='Место нахождения'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='post_address',
            field=models.CharField(max_length=200, verbose_name='Почтовый адрес'),
        ),
    ]