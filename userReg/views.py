from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
# Create your views here.

def index(req):
	return HttpResponse("User Registration Form here")