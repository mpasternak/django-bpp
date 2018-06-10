# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 09:08
from __future__ import unicode_literals

from django.db import migrations

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0132_unique_rekord_id_kolejnosc'),
    ]

    operations = [
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("0134_liczba_cytowan_wyszukaj", *args, **kw)
        ),
    ]
