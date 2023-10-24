from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from vidPlatform.models import DateEntry, Choice, Vote
from django.contrib.auth import get_user_model
from . import emailTesters


def admin_check(user):
    return user.is_superuser


# Create your views here.
@login_required
@user_passes_test(admin_check)
def index(request):
	return render(request, "adminDash/index.html",)


@login_required
@user_passes_test(admin_check)
def emailTest(request):

	return render(request, 'adminDash/emailTest.html')


def emailTestSend(request):
	if request.method == "POST":
		recipient = request.POST.get("recipientInput")

		emailTesters.sendTestEmailTo(recipient)
		
	return redirect("emailTest")


