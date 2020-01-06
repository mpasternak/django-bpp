import django_filters
from django.forms import TextInput, NumberInput

from bpp.models import Cache_Punktacja_Autora_Sum_Gruop, Dyscyplina_Naukowa, Jednostka, Wydzial


class RaportSlotowUczelniaFilter(django_filters.FilterSet):
    autor__nazwisko = django_filters.CharFilter(
        lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Podaj nazwisko'}))

    jednostka = django_filters.CharFilter(
        lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Podaj jednostkę'}))

    jednostka__wydzial = django_filters.ModelChoiceFilter(queryset=Wydzial.objects.all())

    dyscyplina = django_filters.ModelChoiceFilter(queryset=Dyscyplina_Naukowa.objects.all())
    #        lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Podaj nazwę dyscypliny'}))

    slot__min = django_filters.NumberFilter(
        "pkdautslotsum", lookup_expr="gte",
        widget=NumberInput(attrs={"placeholder": "min"}))

    slot__max = django_filters.NumberFilter(
        "pkdautslotsum", lookup_expr="lte",
        widget=NumberInput(attrs={"placeholder": "max"}))

    avg__min = django_filters.NumberFilter(
        "avg", lookup_expr="gte",
        widget=NumberInput(attrs={"placeholder": "min"}))

    avg__max = django_filters.NumberFilter(
        "avg", lookup_expr="lte",
        widget=NumberInput(attrs={"placeholder": "max"}))

    class Meta:
        model = Cache_Punktacja_Autora_Sum_Gruop
        fields = ['autor__nazwisko', 'jednostka', 'dyscyplina__nazwa']
