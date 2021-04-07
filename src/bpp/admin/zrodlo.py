# -*- encoding: utf-8 -*-

# Proste tabele
from dal import autocomplete
from django import forms

from ..models import (  # Publikacja_Habilitacyjna
    Autor,
    Dyscyplina_Zrodla,
    Punktacja_Zrodla,
    Zrodlo,
)
from .core import CommitedModelAdmin
from .filters import PBN_UID_IDObecnyFilter
from .helpers import (
    ADNOTACJE_FIELDSET,
    CHARMAP_SINGLE_LINE,
    MODEL_PUNKTOWANY_BAZA,
    MODEL_PUNKTOWANY_KOMISJA_CENTRALNA,
    ZapiszZAdnotacjaMixin,
)

from django.contrib import admin

from bpp.models.zrodlo import Redakcja_Zrodla

# Źródła indeksowane


class Punktacja_ZrodlaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Punktacja_ZrodlaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ""


class Punktacja_ZrodlaInline(admin.TabularInline):
    model = Punktacja_Zrodla
    form = Punktacja_ZrodlaForm
    fields = ("rok",) + MODEL_PUNKTOWANY_BAZA + MODEL_PUNKTOWANY_KOMISJA_CENTRALNA
    extra = 1


class Redakcja_ZrodlaForm(forms.ModelForm):
    redaktor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        widget=autocomplete.ModelSelect2(url="bpp:autor-autocomplete"),
    )

    model = Redakcja_Zrodla


class Redakcja_ZrodlaInline(admin.TabularInline):
    model = Redakcja_Zrodla
    extra = 1
    form = Redakcja_ZrodlaForm

    class Meta:
        fields = "__all__"


class Dyscyplina_ZrodlaInline(admin.TabularInline):
    model = Dyscyplina_Zrodla
    extra = 1

    class Meta:
        fields = [
            "dyscyplina",
        ]


class ZrodloForm(forms.ModelForm):
    class Meta:
        model = Zrodlo
        widgets = {
            "nazwa": CHARMAP_SINGLE_LINE,
            "skrot": CHARMAP_SINGLE_LINE,
            "nazwa_alternatywna": CHARMAP_SINGLE_LINE,
            "skrot_nazwy_alternatywnej": CHARMAP_SINGLE_LINE,
            "poprzednia_nazwa": CHARMAP_SINGLE_LINE,
        }
        fields = "__all__"


class ZrodloAdmin(ZapiszZAdnotacjaMixin, CommitedModelAdmin):
    form = ZrodloForm

    fields = None
    inlines = (Punktacja_ZrodlaInline, Redakcja_ZrodlaInline, Dyscyplina_ZrodlaInline)
    search_fields = [
        "nazwa",
        "skrot",
        "nazwa_alternatywna",
        "skrot_nazwy_alternatywnej",
        "issn",
        "e_issn",
        "www",
        "poprzednia_nazwa",
        "doi",
        "pbn_uid",
    ]
    autocomplete_fields = ["pbn_uid"]
    list_display = ["nazwa", "skrot", "rodzaj", "www", "issn", "e_issn", "pbn_uid_id"]
    list_filter = [
        "rodzaj",
        "zasieg",
        "openaccess_tryb_dostepu",
        "openaccess_licencja",
        PBN_UID_IDObecnyFilter,
    ]
    list_select_related = ["openaccess_licencja", "rodzaj"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "nazwa",
                    "skrot",
                    "rodzaj",
                    "nazwa_alternatywna",
                    "skrot_nazwy_alternatywnej",
                    "issn",
                    "e_issn",
                    "www",
                    "doi",
                    "pbn_uid",
                    "zasieg",
                    "poprzednia_nazwa",
                    "jezyk",
                    "wydawca",
                ),
            },
        ),
        ADNOTACJE_FIELDSET,
        (
            "OpenAccess",
            {
                "classes": ("grp-collapse grp-closed",),
                "fields": (
                    "openaccess_tryb_dostepu",
                    "openaccess_licencja",
                ),
            },
        ),
    )


admin.site.register(Zrodlo, ZrodloAdmin)
