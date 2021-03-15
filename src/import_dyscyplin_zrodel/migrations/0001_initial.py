# Generated by Django 3.0.11 on 2021-03-15 20:04

import uuid

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import long_running.notification_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bpp", "0250_auto_20210315_2104"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportDyscyplinZrodel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("last_updated_on", models.DateTimeField(auto_now=True)),
                ("started_on", models.DateTimeField(blank=True, null=True)),
                ("finished_on", models.DateTimeField(blank=True, null=True)),
                ("finished_successfully", models.BooleanField(default=False)),
                ("traceback", models.TextField(blank=True, null=True)),
                ("plik_xls", models.FileField(upload_to="")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-last_updated_on"],
                "abstract": False,
            },
            bases=(
                long_running.notification_mixins.ASGINotificationMixin,
                long_running.notification_mixins.NullNotificationMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="ImportDyscyplinZrodelRow",
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
                (
                    "dane_z_xls",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                    ),
                ),
                (
                    "dane_znormalizowane",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="import_dyscyplin_zrodel.ImportDyscyplinZrodel",
                    ),
                ),
                (
                    "zrodlo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="bpp.Zrodlo",
                    ),
                ),
            ],
        ),
    ]
