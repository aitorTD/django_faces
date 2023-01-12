from django.db import models

class Images(models.Model):
    file = models.ImageField(upload_to='pics')
    #description = models.CharField(max_length=200, blank=True)

