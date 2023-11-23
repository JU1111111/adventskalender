from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adminDash.funtions import dbMod
from .views import admin_check


@login_required
@user_passes_test(admin_check)
def leaderboard(request):
	#leaders = dbMod.getCurrentWinners(refresh=True)
	leaders = dbMod.getWinnersUpToYesterday()
	context = {"leaders":leaders}
	return render(request, "adminDash/leaderboard.html",context)