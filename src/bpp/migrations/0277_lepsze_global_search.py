# Generated by Django 3.0.14 on 2021-06-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0276_auto_20210607_0109"),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX bpp_rekord_mat_pbn_uid_id ON bpp_rekord_mat(pbn_uid_id)",
            migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            "CREATE INDEX bpp_autor_search_idx ON bpp_autor  USING GIST (search)",
            migrations.RunSQL.noop,
        ),
    ]
