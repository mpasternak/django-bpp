# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 23:30


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bpp', '0076_auto_20170622_0058'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='publikacja_habilitacyjna',
            unique_together=set([('praca_habilitacyjna', 'content_type', 'object_id')]),
        ),
    ]
