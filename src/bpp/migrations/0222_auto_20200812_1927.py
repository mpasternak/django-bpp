# Generated by Django 3.0.9 on 2020-08-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("bpp", "0221_merge_20200806_0851"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="grant",
            options={"verbose_name": "grant", "verbose_name_plural": "granty"},
        ),
        migrations.RemoveField(model_name="praca_doktorska", name="grant",),
        migrations.RemoveField(model_name="praca_habilitacyjna", name="grant",),
        migrations.RemoveField(model_name="wydawnictwo_ciagle", name="grant",),
        migrations.RemoveField(model_name="wydawnictwo_zwarte", name="grant",),
        migrations.CreateModel(
            name="Grant_Rekordu",
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
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "grant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="bpp.Grant"
                    ),
                ),
            ],
        ),
    ]
