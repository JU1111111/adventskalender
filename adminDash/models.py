from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CorrectUserVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correctVotesNumber = models.IntegerField("number of correct guesses")
