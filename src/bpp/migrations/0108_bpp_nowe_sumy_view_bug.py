# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 09:41
from __future__ import unicode_literals

from django.db import migrations

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):
    dependencies = [
        ('bpp', '0107_poprawki_wydajnosci'),
    ]

    operations = [
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("108_bpp_nowe_sumy_view_bug")
        )
    ]
