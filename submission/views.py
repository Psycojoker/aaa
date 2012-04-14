from artistes.models import Artiste
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def accept(request, pk):
    Artiste.objects.filter(pk=pk).update(published=True)
    return redirect('moderation')

@user_passes_test(lambda u: u.is_superuser)
def reject(request, pk):
    Artiste.objects.filter(pk=pk).update(published=False)
    return redirect('moderation')
