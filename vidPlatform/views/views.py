from django.shortcuts import render, get_object_or_404, redirect
from ..models import DateEntry, Choice, Vote

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib.auth.decorators import login_required
from .viewActive import isActive
from .viewOver import isOver

@login_required
def index(request):
	todaysEntry = DateEntry.objects.filter(start_date__exact=datetime.date.today())
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	yesterdaysEntry = DateEntry.objects.filter(start_date__exact=yesterday)
	latest_list = DateEntry.objects.order_by("start_date")[:24]
	#print(latest_list)
	template = loader.get_template("vidPlatform/index.html")
	context = {
		"latest_list": latest_list,
		"todays_Entry": todaysEntry,
		"yesterdays_Entry": yesterdaysEntry,
	}
	return HttpResponse(template.render(context, request))



@login_required
def detail(request, dateentry_id):
	today = datetime.date.today()

	try:
		dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
	except DateEntry.DoesNotExist:
		raise Http404("date entry doesnt exist")


	if (dateEntry.isActive(today)):
		return isActive(request, dateentry_id)
	
	elif(dateEntry.isInTheFuture(today)):
		return redirect('/advent')
	
	elif (dateEntry.isOver(today)):
		return isOver(request, dateentry_id)
	
	else:
		print("is fucked")
		return Http404("Entry does not exist ")

