# Generated by Django 3.0.11 on 2021-02-28 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("bpp", "0237_auto_20210223_2228"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="autor",
            name="pesel_md5",
        ),
    ]
