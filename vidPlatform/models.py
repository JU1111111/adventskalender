from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class DateEntry(models.Model):
    title = models.CharField(max_length=340, null=True, blank=True)
    pub_date = models.DateTimeField("date published", default=datetime.now())
    start_date = models.DateField("start quiz on")
    end_date = models.DateField("end quiz on")
    videoLink = models.CharField(max_length=340)
    question = models.CharField(max_length=520)



class choice(models.Model):
    question = models.ForeignKey(DateEntry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
