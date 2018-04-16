# -*- enco
# ding: utf-8 -*-
from django.db import transaction
from django.db.models import Sum
from django.views.decorators.cache import never_cache

from multiseek.logic import get_registry
from multiseek.views import MultiseekResults, MULTISEEK_SESSION_KEY_REMOVED, \
    manually_add_or_remove

PKT_WEWN = 'pkt_wewn'
PKT_WEWN_BEZ = 'pkt_wewn_bez'
TABLE = 'table'

EXTRA_TYPES = [PKT_WEWN, PKT_WEWN_BEZ, TABLE]

class MyMultiseekResults(MultiseekResults):
    registry = 'bpp.multiseek.registry'

    def get_queryset(self, only_those_ids=None):
        if only_those_ids:
            qset = get_registry(self.registry).get_query_for_model(
                self.get_multiseek_data()).filter(pk__in=only_those_ids)
        else:
            qset = super(MyMultiseekResults, self).get_queryset()

        flds = ("id",
                "opis_bibliograficzny_cache"
                )

        # wycięte z multiseek/views.py, get_context_data
        public = self.request.user.is_anonymous()
        report_type = get_registry(self.registry).get_report_type(
            self.get_multiseek_data(), only_public=public)


        if report_type in EXTRA_TYPES:
            qset = qset.prefetch_related(
                "charakter_formalny",
                "typ_kbn")

            flds = flds + (
                "charakter_formalny",
                "typ_kbn",
                "punkty_kbn",
                "impact_factor",
                "adnotacje",
                "uwagi",
                "punktacja_wewnetrzna",
                "charakter_formalny__nazwa",
                "typ_kbn__nazwa",
            )

        ret = qset.only(*flds)

        if 'bpp_autorzy_mat' in ret.query.tables or 'bpp_zewnetrzne_bazy_view' in ret.query.tables:
            ret = ret.distinct()

        return ret

    def get_context_data(self, **kwargs):
        t = None

        ctx = super(MyMultiseekResults, self).get_context_data()

        if not self.request.GET.get("print-removed", False):
            qset = self.get_queryset()
        else:
            qset = self.get_queryset(
                only_those_ids=self.request.session.get(
                    MULTISEEK_SESSION_KEY_REMOVED, []))
            ctx['object_list'] = qset
            ctx['print_removed'] = True

        ctx['paginator_count'] = qset.count()
        object_list = ctx['object_list']
        object_list.count = lambda *args, **kw: ctx['paginator_count']

        if ctx['report_type'] in EXTRA_TYPES:
            ctx['sumy'] = qset.aggregate(
                Sum('impact_factor'), Sum('punkty_kbn'),
                Sum('index_copernicus'), Sum('punktacja_wewnetrzna'))

        keys = list(self.request.session.keys())
        if 'MULTISEEK_TITLE' not in keys:
            self.request.session['MULTISEEK_TITLE'] = 'Rezultat wyszukiwania'
        else:
            if self.request.session['MULTISEEK_TITLE'] == '':
                self.request.session['MULTISEEK_TITLE'] = 'Rezultat wyszukiwania'

        return ctx


@never_cache
def bpp_remove_by_hand(request, pk):
    """Add a record's PK to a list of manually removed records.

    User, via the web ui, can add or remove a record to a list of records
    removed "by hand". Those records will be explictly removed
    from the search results in the query function. The list of those
    records is cleaned when there is a form reset.
    """
    pk = tuple([int(x) for x in pk.split("_")])
    return manually_add_or_remove(request, pk)


@never_cache
def bpp_remove_from_removed_by_hand(request, pk):
    """Cancel manual record removal."""
    pk = tuple([int(x) for x in pk.split("_")])
    return manually_add_or_remove(request, pk, add=False)
