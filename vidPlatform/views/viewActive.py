from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..models import DateEntry, Choice, Vote
from vidPlatform.forms import VoteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages


def isActive(request, dateentry_id):
	try:
		dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
		choices = Choice.objects.filter(question=dateEntry).order_by('?')
		alreadyVoted = Vote.objects.filter(choice__in=choices, author=request.user)
	except DateEntry.DoesNotExist:
		raise Http404("date entry doesnt exist")


	if request.method == "POST":
		form = VoteForm(request.POST)

		if form.is_valid():
			vote = form.save(commit=False)
			vote.author = request.user
			if alreadyVoted:
				alreadyVoted.delete()
			vote.save()

		return HttpResponseRedirect(f"/advent/{dateentry_id}/")

	else:
		form = VoteForm()
		choicesField = form.fields['choice']
		choicesField.queryset = choices

		if alreadyVoted:
			choicesField.initial = alreadyVoted[0].choice

		print("yeet")
	return render(request, "vidPlatform/detailPages/detailActive2.html", {"form": form, "entry":dateEntry})