# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0125_auto_20180415_2223'),
        ('import_dyscyplin', '0011_auto_20180415_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='import_dyscyplin_row',
            name='dyscyplina_ostateczna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='bpp.Dyscyplina_Naukowa'),
        ),
    ]
