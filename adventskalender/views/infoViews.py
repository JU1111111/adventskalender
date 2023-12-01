from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

from adminDash.funtions import dbMod


@login_required
def infoView(request):
	return render(request, "adventskalender/infoPage.html")

@login_required
def impressumView(request):
	return render(request, "adventskalender/impressum.html")

@login_required
def privacyNoticeView(request):
	return render(request, "adventskalender/datenschutz.html")

@login_required
def leaderBoardView(request):
	leaders5To8 = dbMod.getCurrentWinners(range(5,9),refresh=True)[:10]
	leaders9To13 = dbMod.getCurrentWinners(range(9,14))[:10]
	context = {"leaders5To8 ":leaders5To8, "leaders9To13":leaders9To13}
	return render(request, "adventskalender/leaderboard.html", context)