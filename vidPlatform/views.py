from django.shortcuts import render, get_object_or_404
from .models import DateEntry
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    latest_list = DateEntry.objects.order_by("-date")[:24]
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
    return render(request,"vidPlatform/detail.html", {"entry":dateEntry} )
