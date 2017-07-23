# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import TemplateView

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

    url(r'^jednostka/$',
        JednostkaRaportFormView.as_view(),
        name='jednostka_form'),

    url(r'^autor/$',
        AutorRaportFormView.as_view(),
        name='autor_form'),

    url(r'autor/(?P<pk>\d+)/(?P<rok>\d+)/',
        GenerujRaportDlaAutora.as_view(),
        name='autor_generuj'),

]
