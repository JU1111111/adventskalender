from vidPlatform.models import DateEntry
from django.shortcuts import render
import datetime


def entryCheck(request):
	entries = DateEntry.objects.all().order_by('start_date')
	okOrNah = []
	activity = []

	currentDate = datetime.date.today()

	for entry in entries:
		if entry.isOK():
			okOrNah.append(True)
		else:
			okOrNah.append(False)

		if entry.isActive(currentDate):
			activity.append("Active")
		elif entry.isInTheFuture(currentDate):
			activity.append("Future")
		elif entry.isOver(currentDate):
			activity.append("Over")
		else:
			activity.append("fucked")

	context = {
		"entries": entries,

	}
	
	return render(request, 'adminDash/entryCheck.html', context)