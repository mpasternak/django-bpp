# Generated by Django 3.0.11 on 2021-01-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0234_rekord_mat_nadrzedne"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="praca_doktorska",
            options={
                "ordering": ("rok", "tytul_oryginalny"),
                "verbose_name": "praca doktorska",
                "verbose_name_plural": "prace doktorskie",
            },
        ),
        migrations.AlterField(
            model_name="wydawnictwo_zwarte",
            name="calkowita_liczba_autorow",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Jeżeli dodajesz monografię, wpisz\n        tutaj całkowitą liczbę autorów monografii. Ta informacja zostanie\n        użyta w eksporcie danych do PBN. Jeżeli informacja ta nie zostanie\n        uzupełiona, wartość tego pola zostanie obliczona i będzie to ilość\n        wszystkich autorów przypisanych do danej monografii",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="wydawnictwo_zwarte",
            name="calkowita_liczba_redaktorow",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Jeżeli dodajesz monografię, wpisz tutaj całkowitą liczbę\n        redaktorów monografii. Ta informacja zostanie użyta w eksporcie\n        danych do PBN. Jeżeli pole to nie zostanie uzupełnione, wartość ta\n        zostanie obliczona i będzie to ilość wszystkich redaktorów\n        przypisanych do danej monografii",
                null=True,
            ),
        ),
    ]