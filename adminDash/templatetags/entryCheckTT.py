from django import template
import datetime
from vidPlatform.models import DateEntry

register = template.Library()


	
@register.simple_tag
def validateIfOK(dateEntry: DateEntry):
	return dateEntry.isOK()

@register.simple_tag
def getState(dateEntry: DateEntry):
	currentDateTime = datetime.date.today()

	if (currentDateTime < dateEntry.start_date):
		return 'in Future'
	elif (currentDateTime >= dateEntry.end_date):
		return 'Past'
	elif (dateEntry.start_date <= currentDateTime < dateEntry.end_date):
		return 'Active'