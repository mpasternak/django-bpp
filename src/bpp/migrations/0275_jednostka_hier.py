# Generated by Django 3.0.14 on 2021-06-06 16:46

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0274_jednostka_hier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jednostka",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="bpp.Jednostka",
                verbose_name="Jednostka nadrzędna",
            ),
        ),
    ]