# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-01 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yurjin_tour', '0047_auto_20161122_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourist',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
    ]