# -*- encoding: utf-8 -*-

from django.urls import path, register_converter
from raport_slotow.converters import DecimalPathConverter
from raport_slotow.views import (
    ParametryRaportSlotowEwaluacja,
    ParametryRaportSlotowUczelnia,
    RaportSlotow,
    RaportSlotowEwaluacja,
    RaportSlotowUczelnia,
    RaportSlotowZerowy,
    WyborOsoby,
)

register_converter(DecimalPathConverter, "decimal")

app_name = "raport_slotow"

urlpatterns = [
    path("raport-slotow-autor/", WyborOsoby.as_view(), name="index"),
    path(
        r"raport-slotow-autor/wyswietl/",
        RaportSlotow.as_view(),
        name="raport",
    ),
    path(
        "raport-slotow-uczelnia/",
        ParametryRaportSlotowUczelnia.as_view(),
        name="index-uczelnia",
    ),
    path(
        "raport-slotow-uczelnia/raport/",
        RaportSlotowUczelnia.as_view(),
        name="raport-uczelnia",
    ),
    path(
        "raport-slotow-ewaluacja/",
        ParametryRaportSlotowEwaluacja.as_view(),
        name="index-ewaluacja",
    ),
    path(
        r"raport-slotow-ewaluacja/raport/",
        RaportSlotowEwaluacja.as_view(),
        name="raport-ewaluacja",
    ),
    path(
        "raport-slotow-zerowy/",
        RaportSlotowZerowy.as_view(),
        name="raport-slotow-zerowy",
    ),
    path(
        "raport-slotow-zerowy/5/",
        RaportSlotowZerowy.as_view(min_pk=5),
        name="raport-slotow-zerowy-bez-5",
    ),
]
