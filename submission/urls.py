from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse

from django.forms.models import modelform_factory
from django.views.generic import CreateView, ListView
from artistes.models import Artiste

class ArtisteCreateView(CreateView):
    model = Artiste
    def get_form_class(self):
        form = modelform_factory(self.model)
        del form.base_fields["published"]
        return form

    def get_success_url(self):
        return reverse("home")

urlpatterns = patterns('submission.views',
    url(r'^$', ArtisteCreateView.as_view(), name='submit'),
    url(r'^moderation/$', ListView.as_view(queryset=Artiste.objects.filter(published=None), template_name="artistes/moderation.html"), name='moderation'),
    url(r'^moderation/accept/(?P<pk>[0-9]+)/$', 'accept', name='accept'),
    url(r'^moderation/reject/(?P<pk>[0-9]+)/$', 'reject', name='reject'),
)
