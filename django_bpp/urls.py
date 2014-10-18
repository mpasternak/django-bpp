# -*- encoding: utf-8 -*-

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, ButtonHolder, Submit
from django.conf.urls import patterns, include, url

import autocomplete_light
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from bpp.views.admin import WydawnictwoCiagleTozView
from bpp.views.mymultiseek import MyMultiseekResults
autocomplete_light.autodiscover()

from django.contrib import admin

admin.autodiscover()


js_info_dict = {
    'packages': ('django.conf',),
}



class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kw):
        self.helper = FormHelper()
        self.helper.form_class = "custom"
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset(
                u'Zaloguj się!',
                'username',
                'password'),
             ButtonHolder(
                Submit('submit', u'Zaloguj się', css_id='id_submit'),
            ))
        AuthenticationForm.__init__(self, request, *args, **kw)


urlpatterns = patterns(
    '',

    url(r'^favicon\.ico$', "bpp.views.favicon"),

    url(r'^dynjs/autorform_dependant.js$', "bpp.views.autorform_dependant_js"),

    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/bpp/wydawnictwo_ciagle/toz/(?P<pk>[\d]+)/$',
        login_required(
            WydawnictwoCiagleTozView.as_view()
        ), name="admin:bpp_wydawnictwo_ciagle_toz"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bpp/', include('bpp.urls', namespace='bpp')),

    url(r'^multiseek/results/$',
        csrf_exempt(MyMultiseekResults.as_view(
            registry=settings.MULTISEEK_REGISTRY,
            template_name="multiseek/results.html"
        )), name="multiseek:results"),

    url(r'^multiseek/', include('multiseek.urls', namespace='multiseek')),
    url(r'^multiseek/live-results/$',
        csrf_exempt(MyMultiseekResults.as_view(
            registry=settings.MULTISEEK_REGISTRY,
            template_name="multiseek/live-results.html"
        )), name="live-results"),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^autocomplete/', include('autocomplete_light.urls'),
        name="autocomplete"),

    url(r'^navigation_autocomplete/$', "bpp.views.navigation_autocomplete",
        name='navigation_autocomplete'),
    url(r'^user_navigation_autocomplete/$',
        "bpp.views.user_navigation_autocomplete",
        name='user_navigation_autocomplete'),

    url(r'^$', "bpp.views.root", name="root"),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        name="login_form", kwargs={'authentication_form':MyAuthenticationForm}),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        name="password_change_done"),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        name="password_change"),

    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),

    (r'^messages/', include('monitio.urls', namespace="monitio")),

    (r'^jsi18n$', 'django.views.i18n.javascript_catalog', js_info_dict),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
