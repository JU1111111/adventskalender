from django import forms
from .models import Vote


class VoteForm(forms.ModelForm):

	class Meta:
		model = Vote
		fields = ["choice"]
		widgets = {
            "choice": forms.RadioSelect(),
        }
		labels = {
            "choice": 'Bitte wählen',
        }


