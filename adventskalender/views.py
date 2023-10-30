from django.shortcuts import  render, redirect
from .forms import NewUserForm, NewStudentForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



def register_request(request):
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		form2 = NewStudentForm(request.POST)
		if form.is_valid() & form2.is_valid():
			print("form's Valid sheeeeeeeeesh")
			userMail = form.data['email']
			username = userMail.replace('.',' ').split('@')[0]
			user = form.save(commit=False)
			user.username = username
			user.last_name = username.split(' ')[-1]
			firstName = ''
			for name in username.split(' ')[:-1]:
				firstName += f' {name}'
			user.first_name = firstName
			user.save()

			student = form2.save(commit=False)
			
			student.user = user
			student.save()
			#student.user = user
			#student.save()

			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/advent/")
		print(form.errors, form2.errors)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	form2 = NewStudentForm
	return render(request, "adventskalender/regPage.html", {"register_form":form, "registerStudent_form":form2})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/advent/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="adventskalender/loginPage.html", context={"login_form":form})



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/advent")


@login_required
def account(request):
	return render(request,"adventskalender/accountPage.html")



@login_required
def infoView(request):
    return render(request, "adventskalender/infoPage.html")
