# Generated by Django 3.0.14 on 2021-05-03 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0009_sentdata"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="conference",
            options={
                "verbose_name": "Konferencja w PBN API",
                "verbose_name_plural": "Konferencje w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="institution",
            options={
                "verbose_name": "Instytucja w PBN API",
                "verbose_name_plural": "Instytucje w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="journal",
            options={
                "verbose_name": "Zródło w PBN API",
                "verbose_name_plural": "Zródła w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="publication",
            options={
                "verbose_name": "Publikacja w PBN API",
                "verbose_name_plural": "Publikacje w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="publisher",
            options={
                "verbose_name": "Wydawca w PBN API",
                "verbose_name_plural": "Wydawcy w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="scientist",
            options={
                "verbose_name": "Osoba w PBN API",
                "verbose_name_plural": "Osoby w PBN API",
            },
        ),
        migrations.AlterModelOptions(
            name="sentdata",
            options={
                "verbose_name": "Informacja o wysłanych danych",
                "verbose_name_plural": "Informacje o wysłanych danych",
            },
        ),
    ]
