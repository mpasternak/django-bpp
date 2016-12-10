# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from model_mommy import mommy

from eksport_pbn.models import PlikEksportuPBN, DATE_CREATED_ON
from eksport_pbn.tasks import eksport_pbn, id_zwartych, id_ciaglych, remove_old_eksport_pbn_files



def test_submit_report_form(admin_app, wydzial):
    page = admin_app.get(reverse("eksport_pbn:zamow"))
    page.form['wydzial'] = wydzial.pk
    res = page.form.submit().maybe_follow()
    assert res.status_code == 200


def test_submit_report_form_validation_data_od_do(admin_app, wydzial):
    page = admin_app.get(reverse("eksport_pbn:zamow"))
    page.form['wydzial'] = wydzial.pk
    page.form['od_daty'] = '2010-01-01'
    page.form['do_daty'] = '2009-01-01'
    res = page.form.submit()
    assert "Wartość w polu &#39;Od daty&#39; musi" in res.content.decode('utf-8')


def test_submit_report_form_validation_rok_od_do(admin_app, wydzial):
    page = admin_app.get(reverse("eksport_pbn:zamow"))
    page.form['wydzial'] = wydzial.pk
    page.form['od_roku'] = '2015'
    page.form['do_roku'] = '2014'
    res = page.form.submit()
    assert "Wartość w polu &#39;Od roku&#39; musi" in res.content.decode('utf-8')


def test_submit_report_form_validation_artykuly_ksiazki(admin_app, wydzial):
    page = admin_app.get(reverse("eksport_pbn:zamow"))
    page.form['wydzial'] = wydzial.pk
    page.form['artykuly'] = False
    page.form['ksiazki'] = False
    page.form['rozdzialy'] = False
    res = page.form.submit()
    assert "Wybierz przynajmniej jedną" in res.content.decode('utf-8')
