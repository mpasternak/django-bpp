import os

import progressbar
from dbfread import DBF
from django.db.models import Q

from bpp import models as bpp
from bpp.models import Status_Korekty, wez_zakres_stron, parse_informacje
from bpp.system import User
from import_dbf import models as dbf
from .codecs import custom_search_function  # noqa

custom_search_function  # noqa


def addslashes(v):
    if not v:
        return v
    if not hasattr(v, 'replace'):
        return v
    return v.replace("'", "''")


def exp_combine(a, b, sep=", "):
    ret = ''
    if a:
        ret = a

    if b:
        if ret:
            ret += sep
        ret += b

    while ret.find("  ") >= 0:
        ret = ret.replace("  ", " ")
    return ret


def import_dbf(filename, appname="import_dbf"):
    tablename = appname + "_" + os.path.basename(filename.split(".")[0]).lower()
    dbf = DBF(filename, encoding="my_cp1250")

    print("BEGIN;")
    print("DROP TABLE IF EXISTS %s;" % tablename)
    print("CREATE TABLE %s(" % tablename)
    for field in dbf.fields:
        print("\t%s text," % field.name.lower())
    print("\t_ignore_me text);")

    for record in dbf:
        print("INSERT INTO %s(%s) VALUES(%s);" % (tablename, ", ".join([f.lower() for f in record]),
                                                  ", ".join(["'%s'" % addslashes(v or '') for v in record.values()])))

    print("COMMIT;")


def exp_parse_str(input):
    """
    :param s: tekst z pola tekstowego bazy danych Expertus, np "#102$ #a$ Tytul #b$ #c$ ...
    :return: słownik zawierający pole 'id' oraz kolejno pola 'a', 'b', 'c' itd
    """
    s = input

    assert len(s) >= 5
    assert s[0] == '#'
    assert s[4] == '$'

    ret = {}

    ret['id'] = int(s[1:4])

    s = s[5:].strip()

    if s[0] != '#':
        raise ValueError(input)

    literki = "abcdefghij"
    cnt = 0

    while True:
        try:
            literka = literki[cnt]
        except IndexError:
            break

        sep = f"#{literka}$"
        pos = s.find(sep)
        if pos < 0:
            # Nie ma takiego separatora w tym ciągu znakw
            continue
        assert pos == 0, "Entry string: %r" % input
        s = s[3:]

        while True:
            try:
                nastepna = literki[cnt + 1]
            except IndexError:
                ret[literka] = s.strip()
                break

            next_pos = s.find(f"#{nastepna}$")
            if next_pos < 0:
                # Nie ma następnego separatora, szukaj kolejnego
                cnt += 1
                continue

            ret[literka] = s[:next_pos].strip()
            break

        s = s[next_pos:]
        cnt += 1

    return ret


def exp_add_spacing(s):
    s = s.replace(".", ". ")
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    s = s.replace(". )", ".)")
    s = s.replace(". -", ".-")
    s = s.replace(". ,", ".,")
    return s.strip()


def integruj_uczelnia(nazwa="Domyślna Uczelnia", skrot="DU"):
    """Jeżeli istnieje jakikolwiek obiekt uczelnia w systemie, zwróć go.

    Jeżeli nie ma żadnych obiektw Uczelnia w systemie, utwórz obiekt z
    ustawieniami domyślnymi i zwróć go. """

    if bpp.Uczelnia.objects.exists():
        return bpp.Uczelnia.objects.first()

    uczelnia, created = bpp.Uczelnia.objects.get_or_create(nazwa=nazwa, skrot=skrot)
    if created:
        User.objects.create_superuser(username="admin", password="admin", email=None)
    return uczelnia


def integruj_wydzialy(uczelnia):
    """Utwórz wydziały na podstawie importu DBF"""
    for wydzial in dbf.Wyd.objects.all():
        bpp.Wydzial.objects.get_or_create(uczelnia=uczelnia, nazwa=wydzial.nazwa, skrot=wydzial.skrot)


def integruj_jednostki(uczelnia):
    for jednostka in dbf.Jed.objects.all():
        if bpp.Jednostka.objects.filter(nazwa=jednostka.nazwa, skrot=jednostka.skrot).exists():
            # Jeżeli istnieje jednostka o dokładnie takiej nazwie, to przejdź dalej
            continue

        widoczna = True
        if jednostka.nazwa == "":
            # Jeżeli nazwa jest pusta, nadaj identyfikator ale i ukryj później
            jednostka.nazwa = "Jednostka %s" % jednostka.idt_jed
            widoczna = False

        while bpp.Jednostka.objects.filter(nazwa=jednostka.nazwa).exists():
            jednostka.nazwa += "*"

        while bpp.Jednostka.objects.filter(skrot=jednostka.skrot).exists():
            jednostka.skrot += "*"

        bpp_jednostka, _ign = bpp.Jednostka.objects.get_or_create(
            nazwa=jednostka.nazwa,
            skrot=jednostka.skrot,
            email=jednostka.email,
            www=jednostka.www,
            wydzial=bpp.Wydzial.objects.get(skrot=jednostka.wyd_skrot),
            uczelnia=uczelnia,
            widoczna=widoczna
        )
        jednostka.bpp_jednostka = bpp_jednostka
        jednostka.save()


def data_or_null(s):
    if s == "15011961":
        return
    if not s:
        return None
    return f"{s[0:4]}-{s[4:6]}-{s[6:8]}"


def get_dict(model, attname):
    return dict([(getattr(i, attname), i) for i in model.objects.all()])


def integruj_tytuly_autorow():
    for tytul, in dbf.Aut.objects.all().order_by().values_list("tytul").distinct("tytul"):
        tytul = tytul.strip()
        if not tytul:
            continue

        tytul = exp_add_spacing(tytul)
        try:
            bpp.Tytul.objects.get(skrot=tytul)
        except bpp.Tytul.DoesNotExist:
            bpp.Tytul.objects.create(nazwa=tytul, skrot=tytul)


def integruj_funkcje_autorow():
    for funkcja, in dbf.Aut.objects.all().order_by().values_list("stanowisko").distinct("stanowisko"):
        funkcja = funkcja.strip()
        if not funkcja:
            continue

        funkcja = exp_add_spacing(funkcja)
        try:
            bpp.Funkcja_Autora.objects.get(nazwa=funkcja)
        except bpp.Funkcja_Autora.DoesNotExist:
            bpp.Funkcja_Autora.objects.create(nazwa=funkcja, skrot=funkcja)


def pbar(query, count):
    return progressbar.progressbar(
        query, max_value=query.count(),
        widgets=[progressbar.AnimatedMarker(), " ",
                 progressbar.SimpleProgress(), " ",
                 progressbar.Timer(), " ",
                 progressbar.ETA()])


def integruj_autorow(uczelnia):
    integruj_tytuly_autorow()
    integruj_funkcje_autorow()

    tytuly = get_dict(bpp.Tytul, "skrot")
    funkcje = get_dict(bpp.Funkcja_Autora, "skrot")

    base_query = dbf.Aut.objects.all()
    count = base_query.count()

    for autor in pbar(base_query.select_related("idt_jed", "idt_jed__bpp_jednostka"), count):
        bpp_autor = None

        if not bpp_autor and autor.exp_id:
            try:
                bpp_autor = bpp.Autor.objects.get(expertus_id=autor.exp_id)
            except bpp.Autor.DoesNotExist:
                pass

        if not bpp_autor and autor.orcid_id:
            try:
                bpp_autor = bpp.Autor.objects.get(orcid=autor.orcid_id)
            except bpp.Autor.DoesNotExist:
                pass

        if not bpp_autor and autor.pbn_id:
            try:
                bpp_autor = bpp.Autor.objects.get(pbn_id=autor.pbn_id)
            except bpp.Autor.DoesNotExist:
                pass

        if bpp_autor is not None:
            # Istnieje już autor z takim ORCID lub PBN ID, nie tworzymy
            autor.bpp_autor = bpp_autor
            autor.save()

        if bpp_autor is None:
            # Nie istnieje taki autor; tworzymy
            tytul = None
            if autor.tytul:
                tytul = tytuly.get(autor.tytul)

            bpp_autor = bpp.Autor.objects.create(
                nazwisko=autor.nazwisk_bz,
                imiona=autor.imiona_bz,
                tytul=tytul,
                pbn_id=autor.pbn_id or None,
                orcid=autor.orcid_id or None,
                expertus_id=autor.exp_id or None
            )

        autor.bpp_autor = bpp_autor
        autor.save()

        # Jeżeli nie ma tego przypisania do jednostki, to utworz:
        if not autor.idt_jed_id:
            continue

        jednostka = autor.idt_jed
        try:
            bpp.Autor_Jednostka.objects.get(autor=bpp_autor, jednostka=jednostka.bpp_jednostka)
        except bpp.Autor_Jednostka.DoesNotExist:
            funkcja_autora = None
            if autor.stanowisko:
                funkcja_autora = funkcje.get(autor.stanowisko)

            bpp.Autor_Jednostka.objects.create(
                autor=bpp_autor,
                jednostka=jednostka.bpp_jednostka,
                funkcja=funkcja_autora,
                rozpoczal_prace=data_or_null(autor.prac_od),
                zakonczyl_prace=data_or_null(autor.dat_zwol)
            )


def integruj_charaktery():
    for rec in dbf.Pub.objects.all():
        try:
            charakter = bpp.Charakter_Formalny.objects.get(skrot=rec.skrot)
        except bpp.Charakter_Formalny.DoesNotExist:
            charakter = bpp.Charakter_Formalny.objects.create(
                nazwa=rec.nazwa,
                skrot=rec.skrot,
            )
        rec.bpp_id = charakter
        rec.save()


def integruj_kbn():
    for rec in dbf.Kbn.objects.all():
        try:
            kbn = bpp.Typ_KBN.objects.get(skrot=rec.skrot)
        except bpp.Typ_KBN.DoesNotExist:
            kbn = bpp.Typ_KBN.objects.create(
                nazwa=rec.nazwa,
                skrot=rec.skrot
            )
        rec.bpp_id = kbn
        rec.save()


def integruj_jezyki():
    for rec in dbf.Jez.objects.all():
        try:
            jez = bpp.Jezyk.objects.get(Q(nazwa=rec.nazwa) | Q(skrot=rec.skrot))
        except bpp.Jezyk.DoesNotExist:
            jez = bpp.Jezyk.objects.create(
                nazwa=rec.nazwa,
                skrot=rec.skrot
            )
        rec.bpp_id = jez
        rec.save()


def integruj_zrodla():
    # pole usm_f:
    # - 988 -> numer ISBN,
    # - 985 -> jakiś identyfikator (dwa rekordy),
    # - 969 -> kilka rekordow nazwanych od okreslen openaccess
    # - 154 -> monografia
    # - 107 -> 10 rekordw (ISSN, numerki, nazwa pracy(?))
    # - 100 -> źrdło indeksowane

    rodzaj = bpp.Rodzaj_Zrodla.objects.get(nazwa='periodyk')

    for rec in dbf.Usi.objects.filter(usm_f='100'):
        rec.nazwa = exp_add_spacing(rec.nazwa)

        try:
            zrodlo = bpp.Zrodlo.objects.get(nazwa=rec.nazwa)
        except bpp.Zrodlo.DoesNotExist:
            zrodlo = bpp.Zrodlo.objects.create(
                nazwa=rec.nazwa,
                skrot=rec.skrot or rec.nazwa,
                rodzaj=rodzaj
            )
        rec.bpp_id = zrodlo
        rec.save()

    for rec in dbf.Usi.objects.filter(usm_f='152'):
        rec.nazwa = exp_add_spacing(rec.nazwa)
        try:
            wydawca = bpp.Wydawca.objects.get(nazwa=rec.nazwa)
        except bpp.Wydawca.DoesNotExist:
            wydawca = bpp.Wydawca.objects.create(
                nazwa=rec.nazwa,
            )
        rec.bpp_wydawca_id = wydawca
        rec.save()

    for rec in dbf.Usi.objects.filter(usm_f='154'):
        rec.nazwa = exp_add_spacing(rec.nazwa)
        try:
            seria = bpp.Seria_Wydawnicza.objects.get(nazwa=rec.nazwa)
        except bpp.Seria_Wydawnicza.DoesNotExist:
            seria = bpp.Seria_Wydawnicza.objects.create(
                nazwa=rec.nazwa,
            )
        rec.bpp_seria_wydawnicza_id = seria
        rec.save()


def integruj_publikacje():
    # zagadnienie nr 1 BPP: prace mają rok i rok_punkt inny: select rok, rok_punkt from import_dbf_bib where rok_punkt != rok and rok_punkt != '' order by rok;

    # zagadnienie nr 2: kody w polach tekstowych:
    #
    # postgres=# select distinct substr(tytul_or, 0, 6) from import_dbf_bib;
    #  substr
    # --------
    #  #102$
    #  #150$
    #  #204$

    # bpp=# select distinct substr(title, 1, 4) from import_dbf_bib;
    #  substr
    # --------
    #  #105
    #  #157
    #  #207

    # postgres=# select distinct substr(zrodlo, 0, 6) from import_dbf_bib;
    #  substr
    # --------
    #  #152$ -> (a: miejsce, b: numer id lub brak, c: rok)
    #  #100$ -> (a: numer id -> idt_usi -> Usi, B_U)
    #  #200$ -> (a: tytuł, b: podtytuł, c: pod red)

    statusy_korekt = dict([(a.nazwa, a) for a in Status_Korekty.objects.all()])
    mapping_korekt = {
        '!': 'przed korektą',
        '*': 'w trakcie korekty',
        'ű': 'po korekcie'
    }

    base_query = dbf.Bib.objects.filter(object_id=None).select_related()

    typy_kbn = dict([(x.skrot, x.bpp_id) for x in dbf.Kbn.objects.all()])
    typ_kbn_pusty = bpp.Typ_KBN.objects.get(skrot='000')

    jezyk_pusty = bpp.Jezyk.objects.get(skrot='000')
    jezyki = dict([(x.skrot, x.bpp_id) for x in dbf.Jez.objects.all()])

    charaktery_formalne = dict([(x.skrot, x.bpp_id) for x in dbf.Pub.objects.all()])

    for rec in pbar(base_query, base_query.count()):
        kw = {}

        poz_a = dbf.Poz.objects.get_for_model(rec.idt, "A")
        if poz_a:
            rec.tytul_or += poz_a

        tytul = exp_parse_str(rec.tytul_or)

        title = None

        if rec.title:
            try:
                title = exp_parse_str(rec.title)
            except ValueError:
                continue

            kw['tytul'] = exp_combine(title.get('a'), title.get('b'), sep=": ")
            for literka in 'cdefgh':
                if literka in title.keys():
                    raise NotImplementedError("co mam z tym zrobic %r" % title)

        kw['charakter_formalny'] = charaktery_formalne[rec.charakter]

        try:
            kw['typ_kbn'] = typy_kbn[rec.kbn]
        except KeyError:
            kw['typ_kbn'] = typ_kbn_pusty

        if not rec.jezyk:
            jez = jezyk_pusty
        else:
            jez = jezyki[rec.jezyk]

        kw['jezyk'] = jez

        if rec.jezyk2:
            kw['jezyk_alt'] = jezyki[rec.jezyk2]

        kw['rok'] = rec.rok
        kw['recenzowana'] = rec.recenzowan.strip() == '1'

        # afiliowana -- nie ma takiego pola
        # kw['afiliowana'] = rec.afiliowana.strip() == '1'

        # kbr -- co to za pole?
        # bpp=# select distinct kbr, count(*) from import_dbf_bib group by kbr;
        #  kbr | count
        # -----+-------
        #      | 86354
        #  000 |    41
        #  OA  |    21
        # (3 rows)

        # lf -- co to za pole?
        # bpp=# select distinct lf, count(*) from import_dbf_bib group by lf;
        #  lf | count
        # ----+-------
        #     |  9605
        #  0  | 66617
        #  1  | 10194
        # (3 rows)

        # study_gr -- co to za pole?
        # bpp=# select distinct study_gr, count(*) from import_dbf_bib group by study_gr;
        #  study_gr | count
        # ----------+-------
        #  0        | 86026
        #  1        |   390
        # (2 rows)

        # idt2 - 5 rekordw

        # pun_max - 1 rekord

        # kwartyl -- co to za pole?
        # bpp=# select distinct kwartyl, count(*) from import_dbf_bib group by kwartyl;
        #  kwartyl | count
        # ---------+-------
        #          | 85236
        #  A       |    37
        #  A1      |   831
        #  B       |    13
        #  B1      |   296
        #  CC      |     3
        # (6 rows)

        # lis_numer -- co to za pole?
        # bpp=# select distinct lis_numer, count(*) from import_dbf_bib group by lis_numer;
        #  lis_numer | count
        # -----------+-------
        #            | 86365
        #  10226     |     1
        #  116       |     8
        #  118       |     1
        #  1436      |     2
        #  157       |     1
        #  162       |     1
        #  165       |     1
        #  167       |     4
        #  182       |     1
        #  205       |     1
        #  22        |     8
        #  2700      |     1
        #  3180      |     1
        #  3903      |     1
        #  4930      |     2
        #  5206      |     1
        #  54        |     3
        #  6728      |     1
        #  75        |     3
        #  756       |     1
        #  7742      |     1
        #  8         |     1
        #  888       |     2
        #  89        |     3
        #  972       |     1
        # (26 rows)

        kw['status_korekty'] = statusy_korekt[mapping_korekt[rec.status]]

        if rec.punkty_kbn:
            kw['punkty_kbn'] = rec.punkty_kbn

        if rec.impact:
            kw['impact_factor'] = rec.impact

        if rec.link:
            kw['www'] = rec.link

        if rec.uwagi2:
            kw['adnotacje'] = rec.uwagi2

        if rec.pun_wl:
            kw['punktacja_wewnetrzna'] = rec.pun_wl

        if rec.issn:
            kw['issn'] = rec.issn

        if rec.eissn:
            kw['e_issn'] = rec.e_issn

        klass = None

        if tytul['id'] == 204:
            klass = bpp.Wydawnictwo_Zwarte
            kw['tytul_oryginalny'] = exp_combine(tytul['a'], tytul.get('b'), sep=": ")

            kw['szczegoly'] = exp_add_spacing(tytul['e'])
            if tytul.get('f'):
                if kw['szczegoly']:
                    kw['szczegoly'] += ", "
                kw['szczegoly'] += tytul['f']

            if tytul.get('c'):
                kw['tytul_oryginalny'] = exp_combine(kw['tytul_oryginalny'], tytul.get('c'))

            if tytul.get('d'):
                kw['tytul_oryginalny'] = exp_combine(kw['tytul_oryginalny'], tytul.get('d'))

            if kw['szczegoly']:
                kw['strony'] = wez_zakres_stron(kw['szczegoly'])

        elif tytul['id'] == 102:
            klass = bpp.Wydawnictwo_Ciagle
            kw['tytul_oryginalny'] = tytul['a']

            if tytul.get("b"):
                kw['tytul_oryginalny'] += ": " + tytul.get("b")

            if tytul.get('c'):
                assert not kw.get('tekst_po_ostatnim_autorze'), (kw, elem, rec)
                kw['tekst_po_ostatnim_autorze'] = tytul.get('c')

            if tytul.get('d') and tytul['d'] != '`':
                assert not kw.get('tytul'), (kw, tytul, rec)
                kw['tytul'] = tytul.get('d')

            for literka in 'ef':
                assert not tytul.get(literka), "co mam robic z %r" % tytul

        elif tytul['id'] == 150:
            klass = bpp.Wydawnictwo_Zwarte
            kw['tytul_oryginalny'] = exp_combine(tytul['a'], exp_combine(tytul.get('b'), tytul.get('d')), sep=" ")
            kw['informacje'] = tytul['c']  # "wstep i oprac. Edmund Waszynski"

        else:
            raise NotImplementedError(tytul)

        # Jeżeli pole 'zrodlo' jest dosc dlugie, reszta tego pola moze znalezc
        # sie w tabeli "Poz" z oznaczeniem literowym 'C'
        zrodlo_cd = dbf.Poz.objects.get_for_model(rec.idt, "C")
        if zrodlo_cd:
            rec.zrodlo += zrodlo_cd

        poz_g = dbf.Poz.objects.get_for_model(rec.idt, "G")
        poz_n = dbf.Poz.objects.get_for_model(rec.idt, "N")

        if poz_g:
            for elem in [elem.strip() for elem in poz_g.split('\r\n') if elem.strip()]:
                elem = exp_parse_str(elem)

                if elem['id'] == 202:
                    wydawca_id = None
                    try:
                        wydawca_id = int(elem['b'][1:])
                    except:
                        pass
                    if wydawca_id is not None:
                        kw['wydawca'] = dbf.Usi.objects.get(idt_usi=wydawca_id).bpp_wydawca_id
                    kw['miejsce_i_rok'] = f"{elem['a']} {elem['c']}"

                elif elem['id'] in [203, 154]:
                    # Seria wydawnicza

                    seria_wydawnicza_id = int(elem['a'][1:])
                    kw['seria_wydawnicza'] = dbf.Usi.objects.get(idt_usi=seria_wydawnicza_id).bpp_seria_wydawnicza_id

                    if elem.get('d') and elem.get('c'):
                        raise NotImplementedError(elem, rec, rec.idt)

                    kw['numer_w_serii'] = ''

                    for literka in "bcd":
                        if elem.get(literka):
                            kw['numer_w_serii'] = exp_combine(kw['numer_w_serii'], elem.get(literka))

                    for literka in "ef":
                        assert not elem.get(literka), (elem, rec)

                elif elem['id'] in [201, 206]:
                    # wydanie
                    kw['uwagi'] = exp_combine(kw.get('uwagi', ''), elem.get('a'), sep=" ")  # Wyd 1 pol
                    kw['uwagi'] = exp_combine(kw.get('uwagi', ''), elem.get('b'), sep=" ")  # pod red A. Kowalski

                    for literka in "cde":
                        assert not elem.get(literka), elem

                elif elem['id'] == 205:

                    isbn = elem['a']
                    if isbn.find("e-ISBN:") >= 0:
                        kw['e_isbn'] = elem['a'].split("e-ISBN:")[1].strip()
                    elif isbn.find("e-ISBN") >= 0:
                        kw['e_isbn'] = elem['a'].split("e-ISBN ")[1].strip()
                    elif isbn.find("ISBN:") >= 0:
                        kw['isbn'] = elem['a'].split("ISBN:")[1].strip()
                    elif isbn.find("ISBN-13") >= 0:
                        kw['isbn'] = elem['a'].split("ISBN-13")[1].strip()
                    elif isbn.find("ISBN") >= 0:
                        kw['isbn'] = elem['a'].split("ISBN ")[1].strip()
                    else:
                        kw['uwagi'] = exp_combine(kw.get('uwagi'), elem.get('a'), sep=", ")

                    for literka in "bcde":
                        assert not elem.get(literka)

                elif elem['id'] == 101:
                    # A: rok,
                    # B: tom
                    # C: numer
                    # D: strony
                    # E: bibliogr. poz

                    kw['informacje'] = elem.get('a')
                    kw['informacje'] = exp_combine(kw['informacje'], elem.get('b'))

                    if elem.get('b'):
                        assert not kw.get('tom')
                        kw['tom'] = elem.get('b')

                    assert not kw.get('szczegoly')
                    kw['szczegoly'] = elem.get('c')
                    if elem.get('d'):
                        if kw['szczegoly']:
                            kw['szczegoly'] += ", "
                        kw['szczegoly'] += elem.get('d')

                    assert not kw.get('uwagi')
                    if elem.get('e'):
                        if kw['szczegoly']:
                            kw['szczegoly'] += ", "
                        kw['szczegoly'] += elem.get('e')

                elif elem['id'] == 103:
                    # Konferencja
                    try:
                        konferencja = bpp.Konferencja.objects.get(nazwa=elem['a'])
                    except bpp.Konferencja.DoesNotExist:
                        konferencja = bpp.Konferencja.objects.create(nazwa=elem['a'])

                    assert not kw.get('konferencja'), (elem, rec)

                    kw['konferencja'] = konferencja
                    for literka in "bcde":
                        assert not elem.get(literka)

                elif elem['id'] == 153:
                    assert not kw.get('szczegoly')
                    kw['szczegoly'] = elem['a']

                    assert not kw.get('uwagi')
                    kw['uwagi'] = exp_combine(elem.get('b'), elem.get('c'))

                elif elem['id'] == 104:
                    assert not kw.get('uwagi'), (kw['uwagi'], elem, rec, rec.idt)
                    kw['uwagi'] = elem['a']
                    for literka in "bcd":
                        assert not elem.get(literka), (elem, rec, rec.idt)

                elif elem['id'] == 151:
                    # w ksiazkach, wydanie i "pod redakcja'
                    if kw['tytul_oryginalny'].find('=') >= 0:
                        raise NotImplementedError
                    kw['tytul_oryginalny'] = (kw['tytul_oryginalny'] + ". " + elem['a'] + " " + elem['b']).strip()

                    for literka in "cde":
                        assert not elem.get(literka), (elem, rec, rec.idt)

                elif elem['id'] in [155, 156]:
                    # 155 "Komunikat tegoż w ... / 156 "toż w wersji polskiej"

                    isbn = elem['a']
                    if isbn.find("e-ISBN:") >= 0:
                        kw['e_isbn'] = elem['a'].split("e-ISBN:")[1].strip()
                    elif isbn.find("e-ISBN") >= 0:
                        kw['e_isbn'] = elem['a'].split("e-ISBN ")[1].strip()
                    elif isbn.find("ISBN:") >= 0:
                        kw['isbn'] = elem['a'].split("ISBN:")[1].strip()
                    elif isbn.find("ISBN") >= 0:
                        kw['isbn'] = elem['a'].split("ISBN")[1].strip()
                    else:
                        assert not kw.get('adnotacje'), (kw, elem, rec)
                        kw['adnotacje'] = elem.get('a')

                elif elem['id'] == 995:
                    assert not kw.get('www'), (elem, rec, kw)
                    kw['www'] = elem['a']
                    for literka in "bcd":
                        assert not elem.get(literka), (elem, rec, rec.idt)

                elif elem['id'] == 991:
                    # DOI
                    kw['doi'] = elem['a']

                elif elem['id'] == 969:
                    # NotImplementedError:
                    # ({'id': 969, 'a': '|0000005187', 'b': '|0000005493', 'c': '|0000005494', 'd': '', 'e': '|0000005496'}, <Bib: Mediators of pruritus in psoriasis>, 38163)
                    # open-access-text-version: FINAL_PUBLISHED
                    # open-access-licence: CC BY
                    # open-access-release-time: AT_PUBLICATION
                    # open-access-article-mode: OPEN_JOURNAL
                    raise NotImplementedError

                else:
                    raise NotImplementedError(elem, rec, rec.idt)

        assert not poz_n, "nie gotowy na poz_n %r %r %s" % (poz_a, rec, rec.idt)

        zrodlo = exp_parse_str(rec.zrodlo)
        if zrodlo['id'] == 200:
            # Wydawnictwo zwarte
            assert klass == bpp.Wydawnictwo_Zwarte

            for literka in 'efg':
                assert not zrodlo.get(literka), "co mam z tym zrobic literka %s w %r" % (literka, zrodlo)

            assert not kw.get('informacje'), (kw['informacje'], rec, rec.idt)
            kw['informacje'] = zrodlo['a']
            if zrodlo.get('b'):
                kw['informacje'] += ": " + zrodlo.get('b')

            if zrodlo.get('c'):
                kw['informacje'] += "; " + zrodlo.get("c")

            if zrodlo.get('d'):
                kw['informacje'] += "; " + zrodlo.get('d')

            if kw['informacje']:
                res = parse_informacje(kw['informacje'], "tom")
                if res:
                    assert not kw.get('tom')
                    kw['tom'] = res

                    # Zwarte NIE ma numeru zeszytu
                # kw['nr_zeszytu'] = parse_informacje(kw['informacje'], "numer")

        elif zrodlo['id'] == 100:
            # Wydawnictwo_Ciagle
            assert klass == bpp.Wydawnictwo_Ciagle
            for literka in 'bcde':
                if literka in zrodlo.keys():
                    raise NotImplementedError("co mam z tym zrobic %r" % zrodlo)

            kw['zrodlo'] = dbf.Usi.objects.get(idt_usi=zrodlo['a'][1:]).bpp_id

        elif zrodlo['id'] == 152:
            # Wydawca indeksowany
            assert klass == bpp.Wydawnictwo_Zwarte

            for literka in "ac":
                # w literce "b" może nie byc tekstu
                assert zrodlo.get(literka), "brak tekstu w literce %s zrodlo %r" % (literka, zrodlo)
            for elem in "def":
                assert elem not in zrodlo.keys()

            if zrodlo.get("b"):
                if kw.get("wydawca"):
                    raise NotImplementedError("Juz jest wydawca, prawdopodobnie z tabeli Poz")
                kw['wydawca'] = dbf.Usi.objects.get(idt_usi=zrodlo['b'][1:]).bpp_wydawca_id

            kw['miejsce_i_rok'] = f"{zrodlo['a']} {zrodlo['c']}"
        else:
            raise NotImplementedError(zrodlo)

        if kw['tytul_oryginalny'].find('=') >= 0 and not (
                kw['tytul_oryginalny'].find('I=532') >= 0
                or kw['tytul_oryginalny'].find('Rudolf Weigl') >= 0
                or kw['tytul_oryginalny'].find('complex = obraz kliniczny, ') >= 0):

            t1, t2 = [x.strip() for x in kw['tytul_oryginalny'].split("=", 1)]

            if kw.get('tytul'):
                if t2 != kw['tytul']:
                    if t1 == kw['tytul']:
                        t1, t2, = t2, t1
                    else:
                        raise NotImplementedError(
                            "jest tytul_oryginalny %r a jest i tytul %r i sie ROZNIA!" % (
                                kw['tytul_oryginalny'], kw['tytul']))

            kw['tytul_oryginalny'] = t1
            kw['tytul'] = t2

        res = klass.objects.create(**kw)

        rec.object = res
        rec.save()


def integruj_b_a():
    base_query = dbf.B_A.objects.filter(object_id=None).exclude(idt__object_id=None)

    for rec in pbar(base_query.select_related(), base_query.count()):
        bpp_rec = rec.idt.object

        bpp_autor = rec.idt_aut.bpp_autor
        bpp_jednostka = rec.idt_jed.bpp_jednostka

        zapisany_jako = f"{rec.idt_aut.imiona} {rec.idt_aut.nazwisko}"

        wxa = bpp_rec.dodaj_autora(bpp_autor, bpp_jednostka, zapisany_jako, afiliuje=rec.afiliacja == '*')

        rec.object = wxa
        rec.save()
