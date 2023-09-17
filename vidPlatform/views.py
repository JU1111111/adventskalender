from django.shortcuts import render, get_object_or_404
from .models import DateEntry
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    todaysEntry = DateEntry.objects.filter(start_date__exact=datetime.date.today())
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterdaysEntry = DateEntry.objects.filter(start_date__exact=yesterday)
    latest_list = DateEntry.objects.order_by("-start_date")[:24]
    template = loader.get_template("vidPlatform/index.html")
    context = {
        "latest_list": latest_list,
        "todays_Entry": todaysEntry,
        "yesterdays_Entry": yesterdaysEntry,
    }
    return HttpResponse(template.render(context, request))



@login_required
def detail(request, dateentry_id):
    print(request.user)
    try:
        dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
    except DateEntry.DoesNotExist:
        raise Http404("date entry doesnt exist")
    
    today = datetime.date.today()

    if (dateEntry.isActive(today)):
        print("is active")
        return render(request,"vidPlatform/detailPages/detailActive.html", {"entry":dateEntry} )
    elif(dateEntry.isInTheFuture(today)):
        print("is in future")
        return render(request,"vidPlatform/detailPages/detailFuture.html", {"entry":dateEntry} )
    elif (dateEntry.isOver(today)):
        print("is over")
        return render(request,"vidPlatform/detailPages/detailOver.html", {"entry":dateEntry} )
    else:
        print("is fucked")
        return Http404("Entry does not exist ")
