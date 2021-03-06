# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-21 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yurjin_tour', '0041_auto_20161121_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touragency',
            name='account',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='Расчетный счет'),
        ),
        migrations.AlterField(
            model_name='touragency',
            name='corr_account',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='Корр. счет'),
        ),
        migrations.AlterField(
            model_name='touragency',
            name='inn',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='touragency',
            name='kpp',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='touragency',
            name='ogrn',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=13, null=True, verbose_name='ОГРН'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='account',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='Расчетный счет'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='corr_account',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='Корр. счет'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='inn',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='kpp',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='ogrn',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=13, null=True, verbose_name='ОГРН'),
        ),
    ]
