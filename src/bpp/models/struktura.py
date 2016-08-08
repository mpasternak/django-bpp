# -*- encoding: utf-8 -*-

"""
Struktura uczelni.
"""
from datetime import datetime

from django.db import models
from autoslug import AutoSlugField
from django.db.models import Q
from djorm_pgfulltext.fields import VectorField

from bpp.util import FulltextSearchMixin
from bpp.models import ModelZAdnotacjami, NazwaISkrot, ModelHistoryczny
from bpp.models.abstract import NazwaWDopelniaczu, ModelZPBN_ID
from bpp.models.autor import Autor, Autor_Jednostka

class Uczelnia(ModelZAdnotacjami, ModelZPBN_ID, NazwaISkrot, NazwaWDopelniaczu):
    slug = AutoSlugField(populate_from='skrot',
        unique=True)
    logo_www = models.ImageField(
        "Logo na stronę WWW", upload_to="logo",
        help_text="""Plik w formacie bitmapowym, np. JPEG lub PNG,
        w rozdzielczości maks. 100x100""", blank=True, null=True)
    logo_svg = models.FileField(
        "Logo wektorowe (SVG)", upload_to="logo_svg",
        blank=True, null=True)
    favicon_ico = models.FileField(
        "Ikona ulubionych (favicon)", upload_to="favicon", blank=True, null=True)

    class Meta:
        verbose_name = "uczelnia"
        verbose_name_plural = "uczelnie"
        app_label = 'bpp'

    def wydzialy(self):
        """Widoczne wydziały -- do pokazania na WWW"""
        return Wydzial.objects.filter(uczelnia=self, widoczny=True)


class Wydzial(ModelZAdnotacjami, ModelZPBN_ID, ModelHistoryczny):
    uczelnia = models.ForeignKey(Uczelnia)
    nazwa = models.CharField(max_length=512, unique=True)
    skrot = models.CharField("Skrót", max_length=4, unique=True)
    opis = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='nazwa',
        max_length=512, unique=True)
    poprzednie_nazwy = models.CharField(max_length=4096, blank=True, null=True, default='')
    kolejnosc = models.IntegerField("Kolejność", default=0)
    widoczny = models.BooleanField(
        default=True,
        help_text="""Czy wydział ma być widoczny przy przeglądaniu strony dla zakładki "Uczelnia"?""")

    zezwalaj_na_ranking_autorow = models.BooleanField(
        "Zezwalaj na generowanie rankingu autorów dla tego wydziału",
        default=True)

    archiwalny = models.BooleanField(
        default=False,
        help_text="""Jeżeli to pole oznaczone jest jako 'PRAWDA', to jednostki 'dawne' - usunięte
        ze struktury uczelni, ale nadal występujące w bazie danych, będą przypisywane do tego wydziału
        przez automatyczne procedury integrujące dane z zewnętrznych systemów informatycznych.
        <br/><br/>
        Jeżeli więcej, niż jeden wydział w bazie ma to pole oznaczone jako 'PRAWDA', jednostki
        przypisywane będą do wydziału o niższym numerze unikalnego identyfikatora (ID)."""
    )

    wirtualny = models.BooleanField(
        default=False, help_text="""Wydział wirtualny to wydział nie mający odzwierciedlenia
        w strukturach uczelni, utworzony na potrzeby bazy danych. Przykładowo, może być
        to wydział skupiający jednostki dawne lub jednostki typu "Obca jednostka", "Doktoranci".
        Tego typu wydział musi być zarządzany ręcznie - nie będzie usuwany, ukrywany ani aktualizowany
        przez procedury importujące dane z zewnętrznych systemów. """)

    class Meta:
        verbose_name = u"wydział"
        verbose_name_plural = u"wydziały"
        ordering = ['kolejnosc', 'skrot']
        app_label = 'bpp'

    def __unicode__(self):
        return self.nazwa

    def jednostki(self):
        """Lista jednostek - dla WWW"""
        return Jednostka.objects.filter(wydzial=self, widoczna=True)

class JednostkaManager(FulltextSearchMixin, models.Manager):
    pass

class Jednostka(ModelZAdnotacjami, ModelZPBN_ID, ModelHistoryczny):
    wydzial = models.ForeignKey(Wydzial, verbose_name="Wydział")
    nazwa = models.CharField(max_length=512, unique=True)
    skrot = models.CharField("Skrót", max_length=128, unique=True)
    opis = models.TextField(blank=True, null=True)
    slug = AutoSlugField(
        populate_from='nazwa',
        unique=True)

    widoczna = models.BooleanField(default=True, db_index=True)
    wchodzi_do_raportow = models.BooleanField(
        "Wchodzi do raportów", default=True, db_index=True)
    email = models.EmailField("E-mail", max_length=128, blank=True, null=True)
    www = models.URLField("WWW", max_length=1024, blank=True, null=True)

    wirtualna = models.BooleanField(
        default=False, help_text="""Jednostka wirtualna to jednostka nie mająca odzwierciedlenia
        w strukturach uczelni, utworzona jedynie na potrzeby bazy danych. Przykładowo, może być
        to "Obca jednostka" - dla autorów nieindeksowanych, lub też może być to jednostka "Doktoranci".
        Tego typu jednostka musi być zarządzana ręcznie od strony strukturalnej - nie będzie
        ukrywana, usuwana ani zmieniana przez procedury importujące dane z zewnętrznych systemów. """)

    obca_jednostka = models.BooleanField(
        default=False, help_text="""Zaznacz dla jednostki skupiającej autorów nieindeksowanych,
        np. dla "Obca jednostka" lub "Doktoranci".

                <br/><br/>
        Jeżeli więcej, niż jedna jednostka w bazie danych ma to pole oznaczone jako 'PRAWDA', autorzy
        przypisywani będą do jednostki obcej o niższym numerze unikalnego identyfikatora (ID).
        """
    )

    search = VectorField(blank=True, null=True)
    objects = JednostkaManager()

    class Meta:
        verbose_name = 'jednostka'
        verbose_name_plural = 'jednostki'
        ordering = ['nazwa']
        app_label = 'bpp'

    def __unicode__(self):
        ret = self.nazwa

        try:
            wydzial = self.wydzial
        except: # TODO catch-all
            wydzial = None

        if wydzial is not None:
            ret += u" (%s)" % self.wydzial.skrot

        return ret

    def dodaj_autora(self, autor, funkcja=None, rozpoczal_prace=None, zakonczyl_prace=None):
        return Autor_Jednostka.objects.create(
            autor=autor, jednostka=self, funkcja=funkcja,
            rozpoczal_prace=rozpoczal_prace, zakonczyl_prace=zakonczyl_prace)

    zatrudnij = dodaj_autora

    def obecni_autorzy(self):
        dzis = datetime.now().date()

        return Autor.objects.filter(
            Q(autor_jednostka__zakonczyl_prace__gte=dzis) | Q(autor_jednostka__zakonczyl_prace=None),
            Q(autor_jednostka__rozpoczal_prace__lte=dzis) | Q(autor_jednostka__rozpoczal_prace=None),
            autor_jednostka__jednostka=self
        ).distinct()

    pracownicy = obecni_autorzy

    def kierownik(self):
        try:
            return self.obecni_autorzy().get(autor_jednostka__funkcja__nazwa='kierownik')
        except Autor.DoesNotExist:
            return None

    def prace_w_latach(self):
        from bpp.models.cache import Rekord
        return Rekord.objects.prace_jednostki(self).values_list(
            'rok', flat=True).distinct().order_by('rok')
