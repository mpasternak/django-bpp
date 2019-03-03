# Generated by Django 2.1.7 on 2019-03-03 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0152_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='aktualna_funkcja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aktualna_funkcja', to='bpp.Funkcja_Autora'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='aktualna_jednostka',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aktualna_jednostka', to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='plec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Plec'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='tytul',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Tytul'),
        ),
        migrations.AlterField(
            model_name='autor_dyscyplina',
            name='dyscyplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Dyscyplina_Naukowa'),
        ),
        migrations.AlterField(
            model_name='autor_jednostka',
            name='funkcja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Funkcja_Autora'),
        ),
        migrations.AlterField(
            model_name='bppuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='charakter_formalny',
            name='charakter_pbn',
            field=models.ForeignKey(blank=True, default=None, help_text='Wartość wybrana w tym polu zostanie użyta jako zawartość tagu <is>\n                                      w plikach eksportu do PBN', null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Charakter_PBN', verbose_name='Charakter PBN'),
        ),
        migrations.AlterField(
            model_name='jednostka',
            name='uczelnia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Uczelnia'),
        ),
        migrations.AlterField(
            model_name='jednostka',
            name='wydzial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Wydzial', verbose_name='Wydział'),
        ),
        migrations.AlterField(
            model_name='jednostka_wydzial',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='jednostka_wydzial',
            name='wydzial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Wydzial'),
        ),
        migrations.AlterField(
            model_name='nagroda',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='nagroda',
            name='organ_przyznajacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.OrganPrzyznajacyNagrody'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='informacja_z',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zrodlo_Informacji'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='rodzaj_prawa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Rodzaj_Prawa_Patentowego'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='status_korekty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Status_Korekty'),
        ),
        migrations.AlterField(
            model_name='patent_autor',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Autor'),
        ),
        migrations.AlterField(
            model_name='patent_autor',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='patent_autor',
            name='typ_odpowiedzialnosci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_Odpowiedzialnosci', verbose_name='Typ odpowiedzialności'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='informacja_z',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zrodlo_Informacji'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='jezyk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jezyk', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='promotor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promotor_doktoratu', to='bpp.Autor'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='status_korekty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Status_Korekty'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='typ_kbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_KBN', verbose_name='Typ KBN'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='informacja_z',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zrodlo_Informacji'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='jezyk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jezyk', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='status_korekty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Status_Korekty'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='typ_kbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_KBN', verbose_name='Typ KBN'),
        ),
        migrations.AlterField(
            model_name='publikacja_habilitacyjna',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'bpp'), ('model', 'wydawnictwo_ciagle')), models.Q(('app_label', 'bpp'), ('model', 'wydawnictwo_zwarte')), models.Q(('app_label', 'bpp'), ('model', 'patent')), _connector='OR'), on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='publikacja_habilitacyjna',
            name='praca_habilitacyjna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Praca_Habilitacyjna'),
        ),
        migrations.AlterField(
            model_name='redakcja_zrodla',
            name='redaktor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Autor'),
        ),
        migrations.AlterField(
            model_name='typ_kbn',
            name='charakter_pbn',
            field=models.ForeignKey(blank=True, default=None, help_text='Wartość wybrana w tym polu zostanie użyta jako \n        fallback, tzn. jeżeli dla charakteru formalnego danego rekordu nie \n        określono odpowiedniego charakteru PBN, to zostanie użyta wartość \n        tego pola, o ile wybrana. ', null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Charakter_PBN', verbose_name='Charakter PBN'),
        ),
        migrations.AlterField(
            model_name='uczelnia',
            name='obca_jednostka',
            field=models.ForeignKey(blank=True, help_text='\n    Jednostka skupiająca autorów nieindeksowanych, nie będących pracownikami uczelni. Procedury importujące\n    dane z zewnętrznych systemów informatycznych będą przypisywać do tej jednostki osoby, które zakończyły\n    pracę na uczelni. ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='obca_jednostka', to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='charakter_formalny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Charakter_Formalny', verbose_name='Charakter formalny'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='informacja_z',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zrodlo_Informacji'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='jezyk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jezyk', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='konferencja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Konferencja'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='openaccess_czas_publikacji',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Czas_Udostepnienia_OpenAccess', verbose_name='OpenAccess: czas udostępnienia'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='openaccess_licencja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Licencja_OpenAccess', verbose_name='OpenAccess: licencja'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='openaccess_tryb_dostepu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Tryb_OpenAccess_Wydawnictwo_Ciagle', verbose_name='OpenAccess: tryb dostępu'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='openaccess_wersja_tekstu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Wersja_Tekstu_OpenAccess', verbose_name='OpenAccess: wersja tekstu'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='status_korekty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Status_Korekty'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='typ_kbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_KBN', verbose_name='Typ KBN'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle_autor',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Autor'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle_autor',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle_autor',
            name='typ_odpowiedzialnosci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_Odpowiedzialnosci', verbose_name='Typ odpowiedzialności'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle_zewnetrzna_baza_danych',
            name='baza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Zewnetrzna_Baza_Danych'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle_zewnetrzna_baza_danych',
            name='rekord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zewnetrzna_baza_danych', to='bpp.Wydawnictwo_Ciagle'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='charakter_formalny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Charakter_Formalny', verbose_name='Charakter formalny'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='informacja_z',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zrodlo_Informacji'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='jezyk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jezyk', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='konferencja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Konferencja'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='openaccess_czas_publikacji',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Czas_Udostepnienia_OpenAccess', verbose_name='OpenAccess: czas udostępnienia'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='openaccess_licencja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Licencja_OpenAccess', verbose_name='OpenAccess: licencja'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='openaccess_tryb_dostepu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Tryb_OpenAccess_Wydawnictwo_Zwarte'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='openaccess_wersja_tekstu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Wersja_Tekstu_OpenAccess', verbose_name='OpenAccess: wersja tekstu'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='seria_wydawnicza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Seria_Wydawnicza'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='status_korekty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Status_Korekty'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='typ_kbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_KBN', verbose_name='Typ KBN'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='wydawnictwo_nadrzedne',
            field=models.ForeignKey(blank=True, help_text='Jeżeli dodajesz rozdział,\n        tu wybierz pracę, w ramach której dany rozdział występuje.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wydawnictwa_powiazane_set', to='bpp.Wydawnictwo_Zwarte'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte_autor',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Autor'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte_autor',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Jednostka'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte_autor',
            name='typ_odpowiedzialnosci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Typ_Odpowiedzialnosci', verbose_name='Typ odpowiedzialności'),
        ),
        migrations.AlterField(
            model_name='wydzial',
            name='uczelnia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Uczelnia'),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='jezyk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Jezyk'),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='openaccess_licencja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bpp.Licencja_OpenAccess', verbose_name='OpenAccess: licencja'),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bpp.Rodzaj_Zrodla'),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='zasieg',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bpp.Zasieg_Zrodla'),
        ),
    ]
