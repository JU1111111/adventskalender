from django.shortcuts import render, get_object_or_404
from ..models import DateEntry, Choice, Vote
from ..forms import VoteForm
from django.http import Http404


def isOver(request, dateentry_id):
	try:
		dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
		choices = Choice.objects.filter(question=dateEntry).order_by('?')
		alreadyVoted = Vote.objects.filter(choice__in=choices, author=request.user)
		correctChoice = choices.filter(isCorrect=True)
	except DateEntry.DoesNotExist:
		raise Http404("date entry doesnt exist")

	#form = VoteForm()
	#choicesField = form.fields['choice']
	#choicesField.queryset = choices
	#choicesField.disabled = True

	
	if alreadyVoted:
		voted = alreadyVoted[0].choice
	else:
		voted = None

	#renderedForm = 	form.render("vidPlatform/snippets/voteFormsnippet.html")

	context = {"entry":dateEntry, "choices":choices, "votedFor":voted}
	return render(request,"vidPlatform/detailPages/detailOver.html", context=context)