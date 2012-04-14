from artistes.models import Artiste
from django.shortcuts import redirect

def accept(request, pk):
    Artiste.objects.filter(pk=pk).update(published=True)
    return redirect('moderation')

def reject(request, pk):
    Artiste.objects.filter(pk=pk).update(published=False)
    return redirect('moderation')
