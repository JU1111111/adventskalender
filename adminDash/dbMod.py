from datetime import timedelta
from vidPlatform.models import DateEntry, Choice, Vote

def changeDateOfAllEntries(DaysToAdd):
	timeDelt = timedelta(days=DaysToAdd)
	entries = DateEntry.objects.all()

	for entry in entries:
		entry.start_date += timeDelt
		entry.end_date += timeDelt
		print(f'changed entry date from {entry.start_date - timeDelt} to {entry.start_date}')