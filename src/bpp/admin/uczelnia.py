from django.contrib import admin

from .core import CommitedModelAdmin
from .core import RestrictDeletionToAdministracjaGroupMixin
from .helpers import *
from ..models import Uczelnia, Wydzial


# Uczelnia

class WydzialInlineForm(forms.ModelForm):
    class Meta:
        fields = ['nazwa', 'skrot', 'widoczny', 'kolejnosc']
        model = Wydzial
        widgets = {'kolejnosc': forms.HiddenInput}


class WydzialInline(admin.TabularInline):
    model = Wydzial
    form = WydzialInlineForm
    extra = 0
    sortable_field_name = 'kolejnosc'


class UczelniaAdmin(RestrictDeletionToAdministracjaGroupMixin,
                    ZapiszZAdnotacjaMixin, CommitedModelAdmin):
    list_display = ['nazwa', 'nazwa_dopelniacz_field', 'skrot', 'pbn_id']
    fieldsets = (
        (None, {
            'fields': (
                'nazwa',
                'nazwa_dopelniacz_field',
                'skrot',
                'pbn_id',
                'favicon_ico',
                'obca_jednostka',
            )}),
        ('Strona wizualna', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'logo_www',
                'logo_svg',
                'pokazuj_punktacje_wewnetrzna',
                'pokazuj_index_copernicus',
                'pokazuj_status_korekty',
                'pokazuj_ranking_autorow',
                'pokazuj_raport_autorow',
                'pokazuj_raport_jednostek',
                'pokazuj_raport_wydzialow',
                'pokazuj_raport_dla_komisji_centralnej',
                'pokazuj_praca_recenzowana'
            )}),
        ADNOTACJE_FIELDSET,
        ('Clarivate Analytics API', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'clarivate_username',
                'clarivate_password'
            )
        })
    )

    inlines = [WydzialInline, ]


admin.site.register(Uczelnia, UczelniaAdmin)