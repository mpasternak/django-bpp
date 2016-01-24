# -*- encoding: utf-8 -*-

from celery.utils.log import get_task_logger
from django.core.management import call_command
from django.core.urlresolvers import reverse
from requests.exceptions import ConnectionError

from bpp.util import remove_old_objects
from django_bpp.util import wait_for_object
from integrator2.models.lista_ministerialna import ListaMinisterialnaIntegration

logger = get_task_logger(__name__)
from django_bpp.celery_tasks import app


@app.task
def analyze_file(klass, pk):
    obj = wait_for_object(klass, pk)

    def informuj(komunikat, dont_persist=True):
        try:
            msg = u'<a href="%s">Integracja pliku "%s": %s</a>. '
            url = reverse("integrator2:detail", args=(obj._meta.model_name, obj.pk,))
            call_command('send_message', obj.owner, msg % (url, obj.filename(), komunikat), dont_persist=dont_persist)
        except ConnectionError, e:
            pass
        except Exception, e:
            obj.extra_info = str(e)
            obj.status = 3
            obj.save()
            raise

    obj.status = 1
    obj.save()

    try:
        obj.dict_stream_to_db()
    except Exception, e:
        obj.extra_info = str(e)
        obj.status = 3
        obj.save()

        informuj(u"wystąpił błąd na etapie importu danych")
        raise

    informuj(u"zaimportowano, trwa analiza danych")

    try:
        obj.match_records()
    except Exception, e:
        obj.extra_info = str(e)
        obj.status = 3
        obj.save()

        informuj(u"wystąpił błąd na etapie matchowania danych")
        raise

    informuj(u"rozpoczęto integrację")

    try:
        obj.integrate()
    except Exception, e:
        obj.extra_info = str(e)
        obj.status = 3
        obj.save()
        informuj(u"wystąpił błąd na etapie integracji danych")
        raise

    obj.status = 2
    obj.save()

    informuj(u"zakończono integrację", dont_persist=False)


@app.task
def remove_old_integrator_files():
    return remove_old_objects(ListaMinisterialnaIntegration, field_name="uploaded_on")
