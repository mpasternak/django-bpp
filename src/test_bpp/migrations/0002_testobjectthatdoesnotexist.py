# Generated by Django 3.0.11 on 2021-03-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_bpp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestObjectThatDoesNotExist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
