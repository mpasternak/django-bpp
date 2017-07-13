# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0081_konferencje'),
    ]

    operations = [
        migrations.AddField(
            model_name='wydawnictwo_ciagle',
            name='liczba_arkuszy_wydawniczych',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Liczba arkuszy wydawniczych'),
        ),
        migrations.AlterField(
            model_name='konferencja',
            name='skrocona_nazwa',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True, verbose_name='Skrócona nazwa'),
        ),
    ]
