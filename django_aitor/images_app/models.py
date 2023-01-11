from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='pics')
    #description = models.CharField(max_length=200, blank=True)