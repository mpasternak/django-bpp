# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0086_calkowita_liczba_redaktorow'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='pokazuj_index_copernicus',
            field=models.BooleanField(default=True, verbose_name='Pokazuj Index Copernicus na stronie rekordu'),
        ),
        migrations.AddField(
            model_name='uczelnia',
            name='pokazuj_punktacje_wewnetrzna',
            field=models.BooleanField(default=True, verbose_name='Pokazuj punktację wewnętrzną na stronie rekordu'),
        ),
    ]
