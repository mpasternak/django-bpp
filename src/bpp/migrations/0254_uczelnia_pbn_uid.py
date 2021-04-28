# Generated by Django 3.0.11 on 2021-04-06 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0007_publication"),
        ("bpp", "0253_rekord_mat_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="uczelnia",
            name="pbn_uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pbn_api.Institution",
            ),
        ),
    ]
