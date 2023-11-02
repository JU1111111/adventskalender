from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
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


