# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0124_auto_20180414_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor_dyscyplina',
            options={'verbose_name': 'powiązanie autora z dyscypliną naukową', 'verbose_name_plural': 'powiązania autorów z dyscyplinami naukowymi'},
        ),
        migrations.AlterModelOptions(
            name='dyscyplina_naukowa',
            options={'verbose_name': 'dyscyplina naukowa', 'verbose_name_plural': 'dyscypliny naukowe'},
        ),
    ]