# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egeriaimport',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
