# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-23 08:28
from __future__ import unicode_literals

import bpp.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0109_rekordview'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='pokazuj_praca_recenzowana',
            field=bpp.models.fields.OpcjaWyswietlaniaField(choices=[('always', 'zawsze'), ('logged-in', 'tylko dla zalogowanych'), ('never', 'nigdy')], default='always', max_length=50, verbose_name='Pokazuj opcję "Praca recenzowana"'),
        ),
    ]
