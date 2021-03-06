# Generated by Django 3.0.11 on 2021-03-15 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0250_auto_20210315_2104"),
        ("import_dyscyplin_zrodel", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="importdyscyplinzrodelrow",
            name="dane_znormalizowane",
        ),
        migrations.CreateModel(
            name="ImportDyscyplinZrodelRowDyscypliny",
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
                    "dyscyplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bpp.Dyscyplina_Naukowa",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="import_dyscyplin_zrodel.ImportDyscyplinZrodelRow",
                    ),
                ),
            ],
        ),
    ]
