import pytest
from django.core.exceptions import ValidationError

from bpp.models import Autor_Dyscyplina, Autor_Jednostka
from raport_slotow.models.uczelnia import (
    RaportSlotowUczelnia,
    RaportSlotowUczelniaWiersz,
)


def test_RaportSlotowUczelnia_get_absolute_url(raport_slotow_uczelnia):
    assert raport_slotow_uczelnia.get_absolute_url()


def test_RaportSlotowUczelnia_clean():
    r = RaportSlotowUczelnia(od_roku=2020, do_roku=2010)
    with pytest.raises(ValidationError):
        r.clean()


def test_RaportSlotowUczelnia_create_report(rekord_slotu, rok, raport_slotow_uczelnia):
    raport_slotow_uczelnia.od_roku = rok
    raport_slotow_uczelnia.do_roku = rok
    raport_slotow_uczelnia.save()

    assert RaportSlotowUczelniaWiersz.objects.count() == 0
    raport_slotow_uczelnia.create_report()

    assert RaportSlotowUczelniaWiersz.objects.count() == 1


def test_RaportSlotowUczelnia_create_report_wszystkie(
    rekord_slotu, rok, raport_slotow_uczelnia
):
    raport_slotow_uczelnia.od_roku = rok
    raport_slotow_uczelnia.do_roku = rok
    raport_slotow_uczelnia.akcja = RaportSlotowUczelnia.Akcje.WSZYSTKO
    raport_slotow_uczelnia.save()

    assert RaportSlotowUczelniaWiersz.objects.count() == 0
    raport_slotow_uczelnia.create_report()

    assert RaportSlotowUczelniaWiersz.objects.count() == 1


@pytest.mark.parametrize(
    "pokazuj_zerowych, expected_rows",
    [
        (False, 1),
        (True, 2),
    ],
)
def test_RaportSlotowUczelnia_zerowi_autorzy(
    rekord_slotu,
    rok,
    autor_jan_nowak,
    autor_jan_kowalski,
    raport_slotow_uczelnia,
    pokazuj_zerowych,
    dyscyplina1,
    expected_rows,
    jednostka,
):
    raport_slotow_uczelnia.od_roku = rok
    raport_slotow_uczelnia.do_roku = rok
    raport_slotow_uczelnia.pokazuj_zerowych = pokazuj_zerowych
    raport_slotow_uczelnia.save()

    # Autor "nie-zerowy", przypisanie do dyscypliny
    Autor_Dyscyplina.objects.create(
        rok=rok, autor=autor_jan_kowalski, dyscyplina_naukowa=dyscyplina1
    )
    Autor_Jednostka.objects.create(autor=autor_jan_kowalski, jednostka=jednostka)

    # Autor "zerowy", przypisanie do dyscypliny
    Autor_Dyscyplina.objects.create(
        rok=rok, autor=autor_jan_nowak, dyscyplina_naukowa=dyscyplina1
    )
    Autor_Jednostka.objects.create(autor=autor_jan_nowak, jednostka=jednostka)

    assert RaportSlotowUczelniaWiersz.objects.count() == 0
    raport_slotow_uczelnia.create_report()

    assert RaportSlotowUczelniaWiersz.objects.count() == expected_rows


def test_RaportSlotowUczelnia_autor_niezerowy_jako_zerowy(
    rekord_slotu,
    rok,
    autor_jan_nowak,
    autor_jan_kowalski,
    raport_slotow_uczelnia,
    dyscyplina1,
    dyscyplina2,
):
    raport_slotow_uczelnia.od_roku = rok
    raport_slotow_uczelnia.do_roku = rok
    raport_slotow_uczelnia.pokazuj_zerowych = True
    raport_slotow_uczelnia.save()

    # Autor "nie-zerowy", przypisanie do dyscypliny - i ma on prace w tej dyscypline (rekord_slotu)
    # do tego przypisanie do sub-dyscypliny w ktorej nie ma prac (zeby był jako zerowy rowniez)
    Autor_Dyscyplina.objects.create(
        rok=rok,
        autor=autor_jan_kowalski,
        dyscyplina_naukowa=dyscyplina1,
        subdyscyplina_naukowa=dyscyplina2,
    )

    # Autor "zerowy", przypisanie do dyscypliny
    Autor_Dyscyplina.objects.create(
        rok=rok, autor=autor_jan_nowak, dyscyplina_naukowa=dyscyplina1
    )

    assert RaportSlotowUczelniaWiersz.objects.count() == 0
    raport_slotow_uczelnia.create_report()

    assert RaportSlotowUczelniaWiersz.objects.count() == 2


def test_RaportSlotowUczelnia_autor_zerowy_w_jednym_roku_niezerowy_w_innym(
    rekord_slotu,
    rok,
    autor_jan_kowalski,
    raport_slotow_uczelnia,
    dyscyplina1,
):
    raport_slotow_uczelnia.od_roku = rok
    raport_slotow_uczelnia.do_roku = rok + 1
    raport_slotow_uczelnia.pokazuj_zerowych = True
    raport_slotow_uczelnia.save()

    Autor_Dyscyplina.objects.create(
        rok=rok,
        autor=autor_jan_kowalski,
        dyscyplina_naukowa=dyscyplina1,
    )
    Autor_Dyscyplina.objects.create(
        rok=rok + 1,
        autor=autor_jan_kowalski,
        dyscyplina_naukowa=dyscyplina1,
    )

    assert RaportSlotowUczelniaWiersz.objects.count() == 0
    raport_slotow_uczelnia.create_report()

    assert RaportSlotowUczelniaWiersz.objects.count() == 1
