from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    pic = models.FileField(upload_to="pics")
    quote = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    published = models.NullBooleanField(default=None)

    class Meta:
        ordering = ['last_name', 'first_name']
