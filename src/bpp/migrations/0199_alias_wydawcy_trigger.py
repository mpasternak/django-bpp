# Generated by Django 2.2.10 on 2020-02-29 22:53

from django.db import migrations

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0198_auto_20200229_1644"),
    ]

    operations = [
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("0199_alias_wydawcy_trigger")
        ),
    ]