# Generated by Django 3.0.11 on 2021-04-06 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0007_publication"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Sciencist",
            new_name="Scientist",
        ),
    ]
