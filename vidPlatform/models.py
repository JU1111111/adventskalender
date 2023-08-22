from django.db import models

# Create your models here.

class dateEntry(models.Model):
    date = models.DateTimeField()
    videoLink = models.CharField(max_length=340)
    
    
