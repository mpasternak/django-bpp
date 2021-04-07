# Generated by Django 3.0.11 on 2021-04-07 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0008_auto_20210406_0530"),
        ("bpp", "0255_auto_20210407_1138"),
    ]

    operations = [
        migrations.AddField(
            model_name="wydawnictwo_ciagle",
            name="pbn_uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pbn_api.Publication",
            ),
        ),
        migrations.AddField(
            model_name="wydawnictwo_zwarte",
            name="pbn_uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pbn_api.Publication",
            ),
        ),
        migrations.AddField(
            model_name="zrodlo",
            name="pbn_uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pbn_api.Journal",
            ),
        ),
    ]
