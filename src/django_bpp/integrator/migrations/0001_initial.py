# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0015_auto_20150617_2247'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorIntegrationFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('file', models.FileField(upload_to=b'integrator', verbose_name=b'Plik')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'dodany'), (1, b'w trakcie analizy'), (2, b'przetworzony')])),
                ('extra_info', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutorIntegrationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tytul_skrot', models.TextField()),
                ('nazwisko', models.TextField()),
                ('imie', models.TextField()),
                ('nazwa_jednostki', models.TextField()),
                ('pbn_id', models.TextField()),
                ('zintegrowano', models.BooleanField(default=False)),
                ('extra_info', models.TextField()),
                ('matching_autor', models.ForeignKey(to='bpp.Autor')),
                ('matching_jednostka', models.ForeignKey(to='bpp.Jednostka')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
