# Generated by Django 3.0.11 on 2021-03-15 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0247_funkcja_autora_pokazuj_za_nazwiskiem"),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS bpp_autorzy_mat_8 ON bpp_autorzy_mat(dyscyplina_naukowa_id, rekord_id);",
            "DROP INDEX IF EXISTS bpp_autorzy_mat_8",
        )
    ]
