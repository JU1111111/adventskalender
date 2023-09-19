from django import template
import datetime
from vidPlatform.models import DateEntry

register = template.Library()



@register.simple_tag
def validateIfActive(dateEntry: DateEntry):
	currentDateTime = datetime.date.today()
	
	if (dateEntry.start_date <= currentDateTime < dateEntry.end_date):
		return True
	else:
		return False
	
@register.simple_tag
def validateIfOver(dateEntry: DateEntry):
	currentDateTime = datetime.date.today()

	if (currentDateTime >= dateEntry.end_date):
		return True
	else:
		return False

@register.simple_tag
def validateIfInTheFuture(dateEntry: DateEntry):
	currentDateTime = datetime.date.today()

	if (currentDateTime < dateEntry.start_date):
		return True
	else:
		return False