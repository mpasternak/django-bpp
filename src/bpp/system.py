# -*- encoding: utf-8 -*-

"""Ustawienia systemowe

groups - lista grup wraz z uprawnieniami do edycji poszczególnych obiektów.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import transaction
from favicon.models import Favicon, FaviconImg
from flexible_reports import models as flexible_models
from multiseek.models import SearchForm
from robots.models import Rule, Url

from bpp.models import (
    Autor,
    Autor_Dyscyplina,
    Autor_Jednostka,
    Charakter_Formalny,
    Dyscyplina_Naukowa,
    Element_Repozytorium,
    Funkcja_Autora,
    Grant,
    Grant_Rekordu,
    Grupa_Pracownicza,
    Jednostka,
    Jezyk,
    Patent,
    Patent_Autor,
    Praca_Doktorska,
    Praca_Habilitacyjna,
    Punktacja_Zrodla,
    Redakcja_Zrodla,
    Rodzaj_Prawa_Patentowego,
    Rodzaj_Zrodla,
    Status_Korekty,
    Typ_KBN,
    Typ_Odpowiedzialnosci,
    Tytul,
    Uczelnia,
    Ukryj_Status_Korekty,
    Wydawnictwo_Ciagle,
    Wydawnictwo_Ciagle_Autor,
    Wydawnictwo_Ciagle_Zewnetrzna_Baza_Danych,
    Wydawnictwo_Zwarte,
    Wydawnictwo_Zwarte_Autor,
    Wydawnictwo_Zwarte_Zewnetrzna_Baza_Danych,
    Wydzial,
    Wymiar_Etatu,
    Zewnetrzna_Baza_Danych,
    Zrodlo,
    Zrodlo_Informacji,
)
from bpp.models.const import GR_WPROWADZANIE_DANYCH
from bpp.models.konferencja import Konferencja
from bpp.models.nagroda import Nagroda, OrganPrzyznajacyNagrody
from bpp.models.openaccess import (
    Czas_Udostepnienia_OpenAccess,
    Licencja_OpenAccess,
    Tryb_OpenAccess_Wydawnictwo_Ciagle,
    Tryb_OpenAccess_Wydawnictwo_Zwarte,
    Wersja_Tekstu_OpenAccess,
)
from bpp.models.praca_habilitacyjna import Publikacja_Habilitacyjna
from bpp.models.profile import BppUser
from bpp.models.seria_wydawnicza import Seria_Wydawnicza
from bpp.models.struktura import Jednostka_Wydzial
from bpp.models.system import Charakter_PBN
from bpp.models.wydawca import Poziom_Wydawcy, Wydawca
from formdefaults.models import FormFieldRepresentation, FormRepresentation
from import_dbf.models import B_A, B_U, Aut, Bib, Ixn, Jed, Poz, Ses, Usi, Wx2
from miniblog.models import Article

User = get_user_model()

groups = {
    "import DBF": [Bib, B_A, Aut, Jed, Poz, B_U, Usi, Ses, Wx2, Ixn],
    "dane systemowe": [
        Charakter_Formalny,
        Charakter_PBN,
        Funkcja_Autora,
        Zrodlo_Informacji,
        Jezyk,
        Typ_Odpowiedzialnosci,
        Rodzaj_Zrodla,
        Status_Korekty,
        Tytul,
        Typ_KBN,
        Tryb_OpenAccess_Wydawnictwo_Ciagle,
        Tryb_OpenAccess_Wydawnictwo_Zwarte,
        Czas_Udostepnienia_OpenAccess,
        Licencja_OpenAccess,
        Wersja_Tekstu_OpenAccess,
        OrganPrzyznajacyNagrody,
        Rodzaj_Prawa_Patentowego,
        Dyscyplina_Naukowa,
        Zewnetrzna_Baza_Danych,
        Grant,
        FormFieldRepresentation,
        FormRepresentation,
        Grupa_Pracownicza,
        Wymiar_Etatu,
    ],
    "struktura": [
        Uczelnia,
        Wydzial,
        Jednostka,
        Jednostka_Wydzial,
        Ukryj_Status_Korekty,
    ],
    GR_WPROWADZANIE_DANYCH: [
        Zrodlo,
        Autor,
        Autor_Dyscyplina,
        Wydawnictwo_Ciagle,
        Wydawnictwo_Zwarte,
        Punktacja_Zrodla,
        Wydawnictwo_Ciagle_Autor,
        Wydawnictwo_Zwarte_Autor,
        Autor_Jednostka,
        Redakcja_Zrodla,
        Praca_Doktorska,
        Praca_Habilitacyjna,
        Patent,
        Patent_Autor,
        Publikacja_Habilitacyjna,
        Konferencja,
        Seria_Wydawnicza,
        Nagroda,
        Wydawnictwo_Ciagle_Zewnetrzna_Baza_Danych,
        Wydawnictwo_Zwarte_Zewnetrzna_Baza_Danych,
        Wydawca,
        Poziom_Wydawcy,
        Grant_Rekordu,
        Element_Repozytorium,
    ],
    "indeks autorów": [Autor, Autor_Jednostka],
    "administracja": [User, Group, SearchForm],
    "web": [Url, Rule, Site, Favicon, FaviconImg, Article],
    "raporty": [
        flexible_models.Report,
        flexible_models.ReportElement,
        flexible_models.Table,
        flexible_models.Column,
        flexible_models.Datasource,
        flexible_models.ColumnOrder,
    ],
}

# Po migracji, upewnij się że robots.txt są generowane poprawnie

DISALLOW_URLS = [
    "/multiseek/",
    "/bpp/raporty/",
    "/eksport_pbn/",
    "/admin/",
    "/integrator2/",
    "/password_change/",
]


def ustaw_robots_txt(**kwargs):
    urls = set()
    for elem in DISALLOW_URLS:
        url, _ignore = Url.objects.get_or_create(pattern=elem)
        urls.add(url)

    cnt = Site.objects.all().count()
    if cnt != 1:
        raise Exception("Not supported count=%i" % cnt)

    r, _ignore = Rule.objects.get_or_create(robot="*")
    r.sites.add(Site.objects.all()[0])
    for elem in DISALLOW_URLS:
        r.disallowed.add(Url.objects.get(pattern=elem))
    r.save()


@transaction.atomic
def odtworz_grupy(**kwargs):
    grp_dict = {}
    for u in BppUser.objects.all():
        grp_dict[u] = [grp.name for grp in u.groups.all()]

    for name, models in list(groups.items()):
        try:
            Group.objects.get(name=name).delete()
        except Group.DoesNotExist:
            pass

        g = Group.objects.create(name=name)
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            for permission in Permission.objects.filter(content_type=content_type):
                g.permissions.add(permission)

    for u, grps in list(grp_dict.items()):
        for gname in grps:
            u.groups.add(Group.objects.get(name=gname))
