from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

class DateEntry(models.Model):
    title = models.CharField(max_length=340, null=True, blank=True)
    pub_date = models.DateTimeField("date published", default=datetime.now())
    start_date = models.DateField("start quiz on")
    end_date = models.DateField("end quiz on")
    videoLink = models.CharField(max_length=64)
    resolutionVidLink = models.CharField(max_length=64)
    question = models.CharField(max_length=520)

    def isInTheFuture(self):
        if (datetime.now < self.start_date):
            return True
        else:
            return False
        
    def isOver(self):
        if (datetime.now > self.end_date):
            return True
        else:
            return False
        
    def isActive(self):
        if (self.start_date <= datetime.date.today() < self.end_date):
            return True
        else:
            return False



class Choice(models.Model):
    question = models.ForeignKey(DateEntry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    isCorrect = models.BooleanField("Is Correct")
    votes = models.IntegerField(default=0)
    

class vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def isCorrect(self):
        if (self.choice.isCorrect):
            return True
        else:
            return False