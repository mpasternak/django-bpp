# Generated by Django 3.0.11 on 2021-04-21 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0008_auto_20210406_0530"),
        ("bpp", "0258_auto_20210407_2320"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jezyk",
            name="skrot_dla_pbn",
        ),
        migrations.AddField(
            model_name="jezyk",
            name="pbn_uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pbn_api.Language",
            ),
        ),
        migrations.AlterField(
            model_name="autor",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="jednostka",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="patent",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="praca_doktorska",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="praca_habilitacyjna",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="uczelnia",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="wydawnictwo_ciagle",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="wydawnictwo_zwarte",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
        migrations.AlterField(
            model_name="wydzial",
            name="pbn_id",
            field=models.IntegerField(
                blank=True,
                db_index=True,
                help_text="[Pole o znaczeniu historycznym] Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
                null=True,
                unique=True,
                verbose_name="[Przestarzałe] Identyfikator PBN",
            ),
        ),
    ]