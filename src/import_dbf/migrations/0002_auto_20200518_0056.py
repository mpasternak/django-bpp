# Generated by Django 3.0.4 on 2020-05-17 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("import_dbf", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bib",
            name="idt2",
            field=models.ForeignKey(
                blank=True,
                db_column="idt2",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="import_dbf.Bib",
            ),
        ),
    ]
