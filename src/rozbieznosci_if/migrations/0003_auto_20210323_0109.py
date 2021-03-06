# Generated by Django 3.0.11 on 2021-03-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rozbieznosci_if", "0002_auto_20210323_0106"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ignorujrozbieznoscif",
            options={"verbose_name": "ignorowanie rozbieżności impact factor"},
        ),
        migrations.AlterField(
            model_name="ignorujrozbieznoscif",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Utworzono"),
        ),
        migrations.AlterField(
            model_name="ignorujrozbieznoscif",
            name="object_id",
            field=models.PositiveIntegerField(db_index=True, verbose_name="Rekord"),
        ),
    ]
