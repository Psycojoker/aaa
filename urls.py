from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import ListView
from artistes.models import Artiste

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Artiste.objects.filter(published=True)), name='home'),
    url(r'^news/', include('basic.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^submission/', include('submission.urls')),
)
