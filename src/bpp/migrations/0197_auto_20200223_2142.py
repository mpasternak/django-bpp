# Generated by Django 2.2.10 on 2020-02-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0196_uczelnia_pokazuj_raport_slotow_zerowy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patent",
            name="strony",
            field=models.CharField(
                blank=True,
                help_text='Jeżeli uzupełnione, to pole będzie eksportowane do \n        danych PBN. Jeżeli puste, informacja ta będzie ekstrahowana z \n        pola "Szczegóły" w chwili generowania eksportu PBN. Aby uniknąć \n        sytuacji, gdy wskutek błędnego wprowadzenia tekstu do pola \n        "Szczegóły" informacja ta nie będzie mogła być wyekstrahowana \n        z tego pola, kliknij przycisk "Uzupełnij", aby spowodować uzupełnienie \n        tego pola na podstawie pola "Szczegóły". \n        ',
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="praca_doktorska",
            name="strony",
            field=models.CharField(
                blank=True,
                help_text='Jeżeli uzupełnione, to pole będzie eksportowane do \n        danych PBN. Jeżeli puste, informacja ta będzie ekstrahowana z \n        pola "Szczegóły" w chwili generowania eksportu PBN. Aby uniknąć \n        sytuacji, gdy wskutek błędnego wprowadzenia tekstu do pola \n        "Szczegóły" informacja ta nie będzie mogła być wyekstrahowana \n        z tego pola, kliknij przycisk "Uzupełnij", aby spowodować uzupełnienie \n        tego pola na podstawie pola "Szczegóły". \n        ',
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="praca_habilitacyjna",
            name="strony",
            field=models.CharField(
                blank=True,
                help_text='Jeżeli uzupełnione, to pole będzie eksportowane do \n        danych PBN. Jeżeli puste, informacja ta będzie ekstrahowana z \n        pola "Szczegóły" w chwili generowania eksportu PBN. Aby uniknąć \n        sytuacji, gdy wskutek błędnego wprowadzenia tekstu do pola \n        "Szczegóły" informacja ta nie będzie mogła być wyekstrahowana \n        z tego pola, kliknij przycisk "Uzupełnij", aby spowodować uzupełnienie \n        tego pola na podstawie pola "Szczegóły". \n        ',
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="uczelnia",
            name="podpowiadaj_dyscypliny",
            field=models.BooleanField(
                default=True,
                help_text='W sytuacji gdy to pole ma wartość "PRAWDA", system będzie podpowiadał dyscyplinę\n        naukową dla powiązania rekordu wydawnictwa i autora w sytuacji, gdy autor ma na dany rok\n        określoną tylko jedną dyscyplinę. W sytuacji przypisania dla autora dwóch dyscyplin na dany rok,\n        pożądaną dyscyplinę będzie trzeba wybrać ręcznie, niezależnie od ustawienia tego pola. ',
            ),
        ),
        migrations.AlterField(
            model_name="wydawnictwo_ciagle",
            name="strony",
            field=models.CharField(
                blank=True,
                help_text='Jeżeli uzupełnione, to pole będzie eksportowane do \n        danych PBN. Jeżeli puste, informacja ta będzie ekstrahowana z \n        pola "Szczegóły" w chwili generowania eksportu PBN. Aby uniknąć \n        sytuacji, gdy wskutek błędnego wprowadzenia tekstu do pola \n        "Szczegóły" informacja ta nie będzie mogła być wyekstrahowana \n        z tego pola, kliknij przycisk "Uzupełnij", aby spowodować uzupełnienie \n        tego pola na podstawie pola "Szczegóły". \n        ',
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="wydawnictwo_zwarte",
            name="strony",
            field=models.CharField(
                blank=True,
                help_text='Jeżeli uzupełnione, to pole będzie eksportowane do \n        danych PBN. Jeżeli puste, informacja ta będzie ekstrahowana z \n        pola "Szczegóły" w chwili generowania eksportu PBN. Aby uniknąć \n        sytuacji, gdy wskutek błędnego wprowadzenia tekstu do pola \n        "Szczegóły" informacja ta nie będzie mogła być wyekstrahowana \n        z tego pola, kliknij przycisk "Uzupełnij", aby spowodować uzupełnienie \n        tego pola na podstawie pola "Szczegóły". \n        ',
                max_length=250,
                null=True,
            ),
        ),
    ]
