from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adminDash.funtions import emailTesters
from .views import admin_check


@login_required
@user_passes_test(admin_check)
def emailTest(request):
	return render(request, 'adminDash/emailTest.html')

@login_required
@user_passes_test(admin_check)
def emailTestSend(request):
	if request.method == "POST":
		recipient = request.POST.get("recipientInput")

		emailTesters.sendTestEmailTo(recipient)
	return redirect("emailTest")