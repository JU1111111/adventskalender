from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adminDash.funtions import dbMod
from .views import admin_check


@login_required
@user_passes_test(admin_check)
def leaderboard(request):
	#leaders = dbMod.getCurrentWinners(refresh=True)
	leaders = dbMod.getCurrentWinners([23,13])

	leaders5To8 = dbMod.getCurrentWinners(range(5,9),refresh=True)
	leaders9To13 = dbMod.getCurrentWinners(range(9,14))
	context = {"leaders5To8 ":leaders5To8, "leaders9To13":leaders9To13}
	return render(request, "adminDash/leaderboard.html",context)