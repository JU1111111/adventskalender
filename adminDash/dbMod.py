from datetime import timedelta
from vidPlatform.models import DateEntry, Choice, Vote

def changeDateOfAllEntries(DaysToAdd):
	timeDelt = timedelta(days=DaysToAdd)
	entries = DateEntry.objects.all()

	for entry in entries:
		entry.start_date += timeDelt
		entry.end_date += timeDelt
		entry.save()