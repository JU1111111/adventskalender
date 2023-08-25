from django.db import models

# Create your models here.

class DateEntry(models.Model):
    date = models.DateTimeField()
    videoLink = models.CharField(max_length=340)

class choice(models.Model):
    question = models.ForeignKey(DateEntry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
