# Generated by Django 2.2.10 on 2020-03-15 19:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0202_auto_20200308_2204"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cache_punktacja_dyscypliny", name="zapisani_wszyscy_autorzy",
        ),
        migrations.AddField(
            model_name="cache_punktacja_dyscypliny",
            name="autorzy_z_dyscypliny",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveIntegerField(),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
