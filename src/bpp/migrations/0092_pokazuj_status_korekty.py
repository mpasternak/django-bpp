# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-19 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0091_charakter_pbn_dla_typu_kbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='pokazuj_status_korekty',
            field=models.BooleanField(default=True, verbose_name='Pokazuj status korekty na stronie rekordu'),
        ),
        migrations.AlterField(
            model_name='charakter_pbn',
            name='wlasciwy_dla',
            field=models.CharField(choices=[('article', 'Artykuł'), ('book', 'Książka'), ('chapter', 'Rozdział')], max_length=20, verbose_name='Właściwy dla...'),
        ),
    ]
