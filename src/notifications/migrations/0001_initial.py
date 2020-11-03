# Generated by Django 3.0.7 on 2020-08-03 18:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("channel_name", models.CharField(db_index=True, max_length=128)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("values", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]