# Generated by Django 2.2.8 on 2020-02-13 20:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("celeryui", "0003_uuid_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="uid",
            field=models.UUIDField(
                blank=True, default=uuid.uuid4, editable=False, unique=True
            ),
        ),
    ]
