# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0114_auto_20171111_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='pokazuj',
            field=models.BooleanField(default=True, help_text='Pokazuj autora na stronach jednostek oraz w rankingu. '),
        ),
    ]
