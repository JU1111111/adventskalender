from django.db import models

# Create your models here.

class dateEntry(models.Model):
    date = models.DateTimeField()
    videoLink = models.CharField(max_length=340)

class choice(models.Model):
    question = models.ForeignKey(dateEntry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
