# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import TemplateView

from nowe_raporty.views import GenerujRaportDlaJednostki, \
    GenerujRaportDlaWydzialu
from .views import GenerujRaportDlaAutora
from .views import WydzialRaportFormView, JednostkaRaportFormView, \
    AutorRaportFormView

urlpatterns = [

    url(r'^index/$',
        TemplateView.as_view(template_name="nowe_raporty/index.html"),
        name='index'),

    url(r'^wydzial/$',
        WydzialRaportFormView.as_view(),
        name='wydzial_form'),

    url(r'wydzial/(?P<pk>\d+)/(?P<od_roku>\d+)/(?P<do_roku>\d+)/',
        GenerujRaportDlaWydzialu.as_view(),
        name='wydzial_generuj'),

    url(r'^jednostka/$',
        JednostkaRaportFormView.as_view(),
        name='jednostka_form'),

    url(r'jednostka/(?P<pk>\d+)/(?P<od_roku>\d+)/(?P<do_roku>\d+)/',
        GenerujRaportDlaJednostki.as_view(),
        name='jednostka_generuj'),

    url(r'^autor/$',
        AutorRaportFormView.as_view(),
        name='autor_form'),

    url(r'autor/(?P<pk>\d+)/(?P<od_roku>\d+)/(?P<do_roku>\d+)/',
        GenerujRaportDlaAutora.as_view(),
        name='autor_generuj'),

]
