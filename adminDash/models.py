from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class CorrectUserVotes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	correctVotesNumber = models.IntegerField("number of correct guesses")
	lastRefresh = models.DateField("letzes Update",  default=timezone.now)
	displayName = models.CharField(max_length=32, default="yeet")
	isStudent = models.BooleanField("is a valid student", default=False)
	currentPlacement = models.SmallIntegerField( 
		validators=[
			MinValueValidator(0)
		], default=0)
