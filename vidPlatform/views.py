from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template("vidPlatform/index.html")
    context={
        "bruh":"yeet"
	}
    return render(request, "vidPlatform/index.html", context)


def detail(request):
    template = loader.get_template("vidPlatform/detail.html")
    context={
        "bruh":"yeet"
	}
    return render(request, "vidPlatform/detail.html", context)