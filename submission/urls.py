from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse

from django.forms.models import modelform_factory
from django.views.generic import CreateView
from artistes.models import Artiste

class ArtisteCreateView(CreateView):
    model = Artiste
    def get_form_class(self):
        form = modelform_factory(self.model)
        del form.base_fields["published"]
        return form

    def get_success_url(self):
        return reverse("home")

urlpatterns = patterns('',
    url(r'^$', ArtisteCreateView.as_view(), name='submit'),
)
