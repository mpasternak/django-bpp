# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('title', models.TextField(verbose_name='Title')),
                ('article_body', model_utils.fields.SplitField(help_text='Use the split marker "&lt;!-- tutaj --&gt;" in case you want to displaythe shorter version of the article body', no_excerpt_field=True, verbose_name='Article body')),
                ('published_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published on')),
                ('slug', models.SlugField(unique=True)),
                ('_article_body_excerpt', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ('-published_on', 'title'),
            },
        ),
    ]