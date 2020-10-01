# Generated by Django 3.0.9 on 2020-09-30 21:49

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FormRepresentation",
            fields=[
                (
                    "full_name",
                    models.TextField(
                        primary_key=True, serialize=False, verbose_name="Kod formularza"
                    ),
                ),
                ("label", models.TextField(verbose_name="Nazwa formularza")),
                (
                    "html_before",
                    models.TextField(
                        blank=True, null=True, verbose_name="Kod HTML przed formularzem"
                    ),
                ),
                (
                    "html_after",
                    models.TextField(
                        blank=True, null=True, verbose_name="Kod HTML po formularzu"
                    ),
                ),
            ],
            options={
                "verbose_name": "Lista wartości domyślnych formularza",
                "verbose_name_plural": "Listy wartości domyślnych formularzy",
                "unique_together": {("full_name", "label")},
            },
        ),
        migrations.CreateModel(
            name="FormFieldRepresentation",
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
                ("name", models.TextField(verbose_name="Systemowa nazwa pola")),
                (
                    "label",
                    models.TextField(
                        blank=True, null=True, verbose_name="Czytelna etykieta pola"
                    ),
                ),
                ("klass", models.TextField(verbose_name="Klasa pola")),
                ("order", models.PositiveSmallIntegerField()),
                (
                    "parent",
                    models.ForeignKey(
                        help_text="Formularz, do którego należy to pole",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fields_set",
                        to="formdefaults.FormRepresentation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pole formularza",
                "verbose_name_plural": "Pola formularzy",
                "ordering": ("order",),
                "unique_together": {("parent", "name")},
            },
        ),
        migrations.CreateModel(
            name="FormFieldDefaultValue",
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
                    "value",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True, verbose_name="Wartość"
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        help_text="Pole formularza, dla którego zdefiniowana jest ta wartość domyślna. ",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="formdefaults.FormFieldRepresentation",
                        verbose_name="Pole formularza",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        help_text="Formularz, do którego należy pole, dla którego to zdefiniowana jestta wartość domyślna pola. ",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="values_set",
                        to="formdefaults.FormRepresentation",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Użytkownik",
                    ),
                ),
            ],
            options={
                "verbose_name": "Wartość domyslna dla pola formularza",
                "verbose_name_plural": "Wartości domyślne dla pól formularzy",
                "ordering": ("user", "field__order"),
            },
        ),
    ]
