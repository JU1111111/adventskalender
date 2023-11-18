from django import forms

class NameForm(forms.Form):
    passwd = forms.CharField()