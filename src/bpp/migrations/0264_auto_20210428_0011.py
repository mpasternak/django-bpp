# Generated by Django 3.0.11 on 2021-04-27 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0263_auto_20210427_2137"),
    ]

    operations = [
        migrations.AddField(
            model_name="uczelnia",
            name="pbn_api_user",
            field=models.ForeignKey(
                blank=True,
                help_text="Użytkownik po stronie BPP który bedzie odpowiedzialny za operacje przeprowadzane w tle przez procesy działające na serwerze i pobierające dane z PBN np w nocy. Jeżeli ten użytkownik dokona autoryzacji w PBN za pomocą przeglądarki, to możliwe będzie również aktualizowanie (wgrywanie) rekordów przez niego na serwer PBN. ",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Użytkownik BPP dla PBN API",
            ),
        ),
        migrations.AlterField(
            model_name="uczelnia",
            name="pbn_aktualizuj_na_biezaco",
            field=models.BooleanField(
                default=False,
                help_text="Aktualizuj rekordy w PBN przy każdym zapisie rekordu. Może spowolnić prace. W przypadku braku dostępu do serwerów PBN nie uniemożliwia edycji rekordów. ",
                verbose_name="Aktualizuj PBN na bieżąco",
            ),
        ),
    ]