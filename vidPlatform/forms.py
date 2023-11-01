from django import forms


class VoteForm(forms.Form):
	choicesField = forms.ModelChoiceField(queryset=None,
									    	empty_label="",
											to_field_name="question",
											widget=forms.RadioSelect,
										  )




