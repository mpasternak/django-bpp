# Generated by Django 3.0.7 on 2020-06-07 16:04

from django.db import migrations, models

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0211_oznaczenie_wydania"),
    ]

    operations = [
        migrations.AddField(
            model_name="patent_autor",
            name="upowaznienie_pbn",
            field=models.BooleanField(
                default=False,
                help_text='Tik w polu "upoważnienie PBN" oznacza, że dany autor upoważnił Uczelnię do sprawozdania tej publikacji w ocenie parametrycznej Uczelni',
                verbose_name="Upoważnienie PBN",
            ),
        ),
        migrations.AddField(
            model_name="wydawnictwo_ciagle_autor",
            name="upowaznienie_pbn",
            field=models.BooleanField(
                default=False,
                help_text='Tik w polu "upoważnienie PBN" oznacza, że dany autor upoważnił Uczelnię do sprawozdania tej publikacji w ocenie parametrycznej Uczelni',
                verbose_name="Upoważnienie PBN",
            ),
        ),
        migrations.AddField(
            model_name="wydawnictwo_zwarte_autor",
            name="upowaznienie_pbn",
            field=models.BooleanField(
                default=False,
                help_text='Tik w polu "upoważnienie PBN" oznacza, że dany autor upoważnił Uczelnię do sprawozdania tej publikacji w ocenie parametrycznej Uczelni',
                verbose_name="Upoważnienie PBN",
            ),
        ),
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("0212_upowaznienie_pbn")
        ),
        # To musi być wczytane, bo "DROP CASCADE" i gubi widoki ewaluacyjne
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("0207_uczelnia_analiza_view")
        ),
    ]
