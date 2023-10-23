from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from vidPlatform.models import DateEntry, Choice, Vote
from django.contrib.auth import get_user_model



def admin_check(user):
    return user.is_superuser


# Create your views here.
@login_required
@user_passes_test(admin_check)
def index(request):
	return render(request, "adminDash/index.html",)


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


def addDaysToDB(request):
	if request.method == "POST":
		numberOfDaysToAdd = request.POST.get("dayAddInput")
		print(numberOfDaysToAdd)

	return redirect("database")