# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-29 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0145_auto_20180629_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uczelnia',
            name='wyszukiwanie_rekordy_na_strone_zalogowany',
            field=models.SmallIntegerField(default=10000, help_text='Ilość rekordów w wyszukiwaniu powyżej której znika opcja"Pokaż wszystkie" i "Drukuj" dla użytkownika zalogowanego. Nie jest zalecane ustawianie powyżej 10000. ', verbose_name='Ilość rekordów na stronę - anonim'),
        ),
    ]
