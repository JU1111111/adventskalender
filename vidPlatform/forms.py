from django import forms
from .models import Vote

class VoteForm(forms.Form):

	class Meta:
		model = Vote
		fields = ("choice", "author")
	