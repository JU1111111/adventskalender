from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..models import DateEntry, Choice, Vote
from vidPlatform.forms import VoteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages


def get_name(request, dateentry_id):
	try:
		dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
		choices = Choice.objects.filter(question=dateEntry)
	except DateEntry.DoesNotExist:
		raise Http404("date entry doesnt exist")


	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		form = VoteForm(request.POST)
		#form.fields['choicesField'].label = ''
		# check whether it's valid:
		#if form.is_valid():
		thechosenone = form.data["ModelChoiceField"]
			#messages.success(request, 'Form submission successful')
		return HttpResponseRedirect(f"/advent/{dateentry_id}/")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = VoteForm()
		form.fields['choicesField'].queryset = choices
		form.fields['choicesField'].label = ''
	print("yeet")
	return render(request, "vidPlatform/detailPages/detailActive2.html", {"form": form, "entry":dateEntry})