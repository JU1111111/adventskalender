from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vidPlatform.models import Student



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "password1", "password2")

	def exists(self):
		user = super(NewUserForm, self).save(commit=False)
		email = self.cleaned_data['email']
		if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
			return True
		user.email = email
		return False

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user
	

class NewStudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ("studentYear", "studentClass")