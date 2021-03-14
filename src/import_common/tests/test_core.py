import pytest
from model_mommy import mommy

from bpp.models import Autor, Jednostka, Tytul, Wydzial
from import_dyscyplin.core import matchuj_autora, matchuj_jednostke, matchuj_wydzial


@pytest.mark.parametrize(
    "szukany_string",
    [
        "II Lekarski",
        "II Lekarski ",
        "ii lekarski",
        "   ii lekarski  ",
    ],
)
def test_matchuj_wydzial(szukany_string, db):
    mommy.make(Wydzial, nazwa="I Lekarski")
    w2 = mommy.make(Wydzial, nazwa="II Lekarski")

    assert matchuj_wydzial(szukany_string) == w2


@pytest.mark.parametrize(
    "szukany_string",
    ["Jednostka Pierwsza", "  Jednostka Pierwsza  \t", "jednostka pierwsza"],
)
def test_matchuj_jednostke(szukany_string, uczelnia, wydzial, db):
    j1 = mommy.make(
        Jednostka, nazwa="Jednostka Pierwsza", wydzial=wydzial, uczelnia=uczelnia
    )
    mommy.make(
        Jednostka,
        nazwa="Jednostka Pierwsza i Jeszcze",
        wydzial=wydzial,
        uczelnia=uczelnia,
    )

    assert matchuj_jednostke(szukany_string) == j1


def test_matchuj_autora_imiona_nazwisko(autor_jan_nowak):
    a = matchuj_autora("Jan", "Nowak", jednostka=None)
    assert a == autor_jan_nowak


@pytest.mark.django_db
def test_matchuj_autora_po_aktualnej_jednostce():
    j1 = mommy.make(Jednostka)
    j2 = mommy.make(Jednostka)

    a1 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a1.dodaj_jednostke(j1)

    a2 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a2.dodaj_jednostke(j2)

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", jednostka=None)
    assert a is None

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", jednostka=j1)
    assert a == a1

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", jednostka=j2)
    assert a == a2


@pytest.mark.django_db
def test_matchuj_autora_po_jednostce():
    j1 = mommy.make(Jednostka)
    j2 = mommy.make(Jednostka)

    a1 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a1.dodaj_jednostke(j1)
    a1.aktualna_jednostka = None
    a1.save()

    a2 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a2.dodaj_jednostke(j2)
    a2.aktualna_jednostka = None
    a2.save()

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", jednostka=j1)
    assert a == a1

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", jednostka=j2)
    assert a == a2


@pytest.mark.django_db
def test_matchuj_autora_po_tytule():
    t = Tytul.objects.create(nazwa="prof hab", skrot="lol.")

    mommy.make(Jednostka)

    a1 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a1.tytul = t
    a1.save()

    mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")

    a = matchuj_autora(
        imiona="Jan",
        nazwisko="Kowalski",
    )
    assert a is None

    a = matchuj_autora(imiona="Jan", nazwisko="Kowalski", tytul_str="lol.")
    assert a == a1


@pytest.mark.django_db
def test_matchuj_autora_tytul_bug(jednostka):
    matchuj_autora("Kowalski", "Jan", jednostka, tytul_str="Doktur")
    assert True