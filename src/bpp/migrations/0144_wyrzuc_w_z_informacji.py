# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bpp', '0143_uczelnia_wydruk_logo_szerokosc'),
    ]

    # Ta migracja NIE może iść przez Django, musi być na poziomie SQL,
    # ponieważ faktyczna zmiana pola "Informacje" doprowadzi do zaktualizowania
    # daty w polu "Ostatnio zmieniony dla PBN" - jeżeli zrobimy to
    # przez Django. Jeżeli jednak zrobimy to przez SQL, to powinno
    # być w porządku...

    operations = [
        migrations.RunSQL(
            """
            UPDATE bpp_wydawnictwo_zwarte SET 
            informacje = TRIM(SUBSTR(informacje, 3))
            WHERE informacje ILIKE 'W:%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_patent SET 
            informacje = TRIM(SUBSTR(informacje, 3))
            WHERE informacje ILIKE 'W:%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_praca_doktorska SET 
            informacje = TRIM(SUBSTR(informacje, 3))
            WHERE informacje ILIKE 'W:%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_praca_habilitacyjna SET 
            informacje = TRIM(SUBSTR(informacje, 3))
            WHERE informacje ILIKE 'W:%';
            """,
            migrations.RunSQL.noop),



        migrations.RunSQL(
            """
            UPDATE bpp_wydawnictwo_zwarte SET 
            informacje = TRIM(SUBSTR(informacje, 4))
            WHERE informacje ILIKE 'W :%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_patent SET 
            informacje = TRIM(SUBSTR(informacje, 4))
            WHERE informacje ILIKE 'W :%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_praca_doktorska SET 
            informacje = TRIM(SUBSTR(informacje, 4))
            WHERE informacje ILIKE 'W :%';
            """,
            migrations.RunSQL.noop),
        migrations.RunSQL(
            """
            UPDATE bpp_praca_habilitacyjna SET 
            informacje = TRIM(SUBSTR(informacje, 4))
            WHERE informacje ILIKE 'W :%';
            """,
            migrations.RunSQL.noop),
    ]
