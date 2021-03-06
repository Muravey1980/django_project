# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0040_auto_20161121_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='tour_agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yurjin_tour.TourAgency'),
        ),
        migrations.AddField(
            model_name='touragency',
            name='account',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, verbose_name='Расчетный счет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touragency',
            name='corr_account',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, verbose_name='Корр. счет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touragency',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AddField(
            model_name='touragency',
            name='kpp',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=9, verbose_name='КПП'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touragency',
            name='phone_num',
            field=models.CharField(blank=True, max_length=200, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='touroperator',
            name='account',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, verbose_name='Расчетный счет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touroperator',
            name='corr_account',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, verbose_name='Корр. счет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touroperator',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AddField(
            model_name='touroperator',
            name='kpp',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=9, verbose_name='КПП'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touroperator',
            name='phone_num',
            field=models.CharField(blank=True, max_length=200, verbose_name='Телефон'),
        ),
    ]
