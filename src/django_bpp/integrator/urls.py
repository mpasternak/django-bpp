from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from django.conf import settings
from integrator.views import FileUploadView, FileListView

urlpatterns = patterns(
    '',

    url(r'^nowy/$', login_required(FileUploadView.as_view(template_name="integrator_upload.html")), name='new'),
    url(r'^$', login_required(FileListView.as_view(template_name="integrator_list.html")), name='list'),

)
