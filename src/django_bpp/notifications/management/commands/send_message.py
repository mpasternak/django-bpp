# -*- encoding: utf-8 -*
from optparse import make_option
from django.core.urlresolvers import reverse
from django.db import transaction

import messages_extends as messages
from django.contrib.auth import get_user_model

from django.core.management import BaseCommand
from django.test import RequestFactory
from messages_extends.storages import PersistentStorage

import notifications
from messages_extends.models import Message


class Command(BaseCommand):
    help = 'Wysyla komunikat offline za pomoca frameworku messages'
    args = '<username> <message>'

    option_list = BaseCommand.option_list + (make_option('--dont-persist',
                                                        action='store_true',
                                                        dest='no_persist',
                                                        default=False,
                                                        help="Don't persist the message"),)

    def handle(self, *args, **options):
        request_factory = RequestFactory()

        request = request_factory.get('/')

        request.user = get_user_model().objects.get(username=args[0])
        setattr(request, 'session', 'session')

        storage = PersistentStorage(request)

        setattr(request, '_messages', storage)

        level = messages.INFO_PERSISTENT
        text = args[1]

        msg = None

        if options['no_persist']:
            notifications.send_notification(
                request, level, text, verbose=int(options['verbosity']) > 1)
            return

        with transaction.atomic():
            messages.add_message(request, level, text)
            msg = Message.objects.filter(user_id=request.user.pk, message=text).order_by('-pk')[:1]

        if msg:
            msg = msg[0]
            closeURL = reverse('messages_extends:message_mark_read', args=(msg.pk,))
            notifications.send_notification(
                request, level, text, verbose=int(options['verbosity']) > 1, closeURL=closeURL)
