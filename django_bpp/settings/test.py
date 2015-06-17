# -*- encoding: utf-8 -*-

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SENDFILE_BACKEND = 'sendfile.backends.simple'

INSTALLED_APPS += ("django_jenkins", )
INSTALLED_APPS += ("django_nose", )

SELENIUM_DRIVER = "Firefox"

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

MEDIA_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'media')
)
SENDFILE_ROOT = MEDIA_ROOT

COMPRESS_OFFLINE = True

# host dla HTMLu oraz linii polecen, reszta dla linii polecen (bo HTML sie autokonfiguruje...)
NOTIFICATIONS_HOST = 'staging-bpp.local'
NOTIFICATIONS_PORT = None
NOTIFICATIONS_PROTOCOL = 'http'
