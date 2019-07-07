# Generated by Django 2.1.7 on 2019-06-29 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0161_dyscyplina_change_trigger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor_dyscyplina',
            name='dyscyplina_naukowa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dyscyplina', to='bpp.Dyscyplina_Naukowa'),
        ),
        migrations.AlterField(
            model_name='autor_dyscyplina',
            name='subdyscyplina_naukowa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subdyscyplina', to='bpp.Dyscyplina_Naukowa'),
        ),
    ]
