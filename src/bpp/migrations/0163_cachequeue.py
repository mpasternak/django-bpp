# Generated by Django 2.1.7 on 2019-07-01 07:14

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bpp', '0162_auto_20190629_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='CacheQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('started_on', models.DateTimeField(blank=True, null=True)),
                ('task_id', models.CharField(blank=True, max_length=36, null=True)),
                ('error', models.BooleanField(default=False)),
                ('info', models.TextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
