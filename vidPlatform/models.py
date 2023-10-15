from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

class DateEntry(models.Model):
    title = models.CharField(max_length=340, null=True, blank=True)
    pub_date = models.DateTimeField("date published", default=datetime.now())
    start_date = models.DateField("start quiz on", help_text="Is active from this day on")
    end_date = models.DateField("end quiz on", help_text="From beginning of this day on no longer active")
    videoLink = models.CharField(max_length=64, help_text="Youtube Video Code only")
    resolutionVidLink = models.CharField(max_length=64, help_text="Youtube Video Code only")
    question = models.CharField(max_length=520)

    def isInTheFuture(self, currentDateTime):
        if (currentDateTime < self.start_date):
            return True
        else:
            return False
        
    def isOver(self, currentDateTime):
        if (currentDateTime >= self.end_date):
            return True
        else:
            return False
        
    def isActive(self, currentDateTime):
        if (self.start_date <= currentDateTime < self.end_date):
            return True
        else:
            return False
        

    def __str__(self):
        name = f"{self.start_date}_{self.title}"
        return name



class Choice(models.Model):
    question = models.ForeignKey(DateEntry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    isCorrect = models.BooleanField("Is Correct", default=False)
    votes = models.IntegerField(default=0)
    

class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def isCorrect(self):
        if (self.choice.isCorrect):
            return True
        else:
            return False