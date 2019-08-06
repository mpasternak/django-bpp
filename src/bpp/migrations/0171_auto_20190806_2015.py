# Generated by Django 2.1.7 on 2019-08-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0170_wydawnictwo_wydawca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poziom_wydawcy',
            options={'verbose_name': 'poziom wydawcy', 'verbose_name_plural': 'poziomy wydawcy'},
        ),
        migrations.AlterField(
            model_name='poziom_wydawcy',
            name='poziom',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(None, 'nieokreślono'), (1, 'poziom I'), (2, 'poziom II')], null=True),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='wydawca_opis',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Wydawca - szczegóły'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='wydawca_opis',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Wydawca - szczegóły'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='wydawca_opis',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Wydawca - szczegóły'),
        ),
    ]
