# Generated by Django 3.0.11 on 2021-04-06 02:01

from django.db import migrations, models

import django.contrib.postgres.fields.jsonb


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("last_updated_on", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("last_updated_on", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("language", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
