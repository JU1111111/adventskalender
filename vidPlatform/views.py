from django.shortcuts import render, get_object_or_404
from .models import DateEntry
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
import datetime

# Create your views here.

def index(request):
    latest_list = DateEntry.objects.order_by("-start_date")[:24]
    template = loader.get_template("vidPlatform/index.html")
    context = {
        "latest_list": latest_list,
    }
    return HttpResponse(template.render(context, request))




def detail(request, dateentry_id):
    try:
        dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
    except DateEntry.DoesNotExist:
        raise Http404("date entry doesnt exist")
    
    today = datetime.date.today()

    if (dateEntry.isActive(today)):
        print("is active")
        return render(request,"vidPlatform/detailActive.html", {"entry":dateEntry} )
    elif(dateEntry.isInTheFuture(today)):
        print("is in future")
        return HttpResponse("not yet available")
    elif (dateEntry.isOver(today)):
        print("is over")
        return HttpResponse("Vote is over. Video and its Resulution here")
    else:
        print("is fucked")
        return Http404("Entry does not exist ")
