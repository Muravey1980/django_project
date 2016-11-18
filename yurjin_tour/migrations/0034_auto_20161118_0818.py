# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0033_auto_20161117_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Турагентства',
                'verbose_name': 'Турагентство',
            },
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_name_r',
            field=models.CharField(blank=True, max_length=200, verbose_name='ФИО в родительном падеже'),
        ),
    ]
