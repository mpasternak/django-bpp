# Generated by Django 3.0.14 on 2021-05-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0010_auto_20210504_0040"),
    ]

    operations = [
        migrations.AddField(
            model_name="sentdata",
            name="exception",
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AddField(
            model_name="sentdata",
            name="uploaded_okay",
            field=models.BooleanField(default=True),
        ),
    ]
