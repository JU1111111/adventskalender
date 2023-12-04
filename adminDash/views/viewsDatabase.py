from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from vidPlatform.models import DateEntry, Vote
from django.contrib.auth import get_user_model
from adminDash.funtions import dbMod
from .views import admin_check


@login_required
@user_passes_test(admin_check)
def database(request):
	numberEntries = DateEntry.objects.all().count()
	User = get_user_model()
	numberUsers = User.objects.all().count()
	numberVotes = Vote.objects.all().count()
	context = {"numEntries": numberEntries,
				"numUsers": numberUsers,
				"numVotes": numberVotes
				}
	return render(request, "adminDash/databaseOptions.html", context)


@login_required
@user_passes_test(admin_check)
def addDaysToDB(request):
	if request.method == "POST":
		numberOfDaysToAdd = request.POST.get("dayAddInput")
		print(type(numberOfDaysToAdd))
		numOfDaysInt = int(numberOfDaysToAdd)
		dbMod.changeDateOfAllEntries(numOfDaysInt)

	return redirect("database")


@login_required
@user_passes_test(admin_check)
def importFromDoc(request):
	dbMod.getDateEntries()
	return redirect("database")