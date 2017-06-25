# -*- encoding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from bpp.models.praca_doktorska import Praca_Doktorska_Baza


class Publikacja_Habilitacyjna(models.Model):
    praca_habilitacyjna = models.ForeignKey('Praca_Habilitacyjna')
    kolejnosc = models.IntegerField('Kolejność', default=0)

    limit = models.Q(app_label='bpp', model='wydawnictwo_ciagle') | \
            models.Q(app_label='bpp', model='wydawnictwo_zwarte') | \
            models.Q(app_label='bpp', model='patent')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    publikacja = GenericForeignKey()

    class Meta:
        app_label = 'bpp'
        verbose_name = u"powiązanie publikacji z habilitacją"
        verbose_name_plural = u"powiązania publikacji z habilitacją"
        unique_together = [
            ('praca_habilitacyjna', 'content_type', 'object_id')
        ]
        ordering = ('kolejnosc',)


class Praca_Habilitacyjna(Praca_Doktorska_Baza):
    publikacje_habilitacyjne = GenericRelation(Publikacja_Habilitacyjna)

    class Meta:
        verbose_name = 'praca habilitacyjna'
        verbose_name_plural = 'prace habilitacyjne'
        app_label = 'bpp'
