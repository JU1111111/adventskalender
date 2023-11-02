from django.shortcuts import  render, redirect
from .forms import NewUserForm, NewStudentForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from adminDash.funtions.emailTesters import getDataFromTheJson
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str



def register_request(request):
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		form2 = NewStudentForm(request.POST)
		if form.is_valid() & form2.is_valid():
			print("form's Valid sheeeeeeeeesh")
			#userMail = form.data['email']
			userMail = form.cleaned_data.get('email')
			username = userMail.replace('.',' ').split('@')[0]
			user = form.save(commit=False)
			user.username = username
			user.last_name = username.split(' ')[-1]
			firstName = ''
			for name in username.split(' ')[:-1]:
				firstName += f' {name}'
			user.first_name = firstName
			user.is_active = False
			user.save()
			student = form2.save(commit=False)
			student.user = user
			student.save()
			
			emailData = getDataFromTheJson()

			current_site = get_current_site(request)
			mail_subject = 'Activate your account.'
			context = {
						'user': user,
						'domain': current_site.domain,
						'uid': urlsafe_base64_encode(force_bytes(user.pk)),
						'token': account_activation_token.make_token(user),
					}
			message = render_to_string('adventskalender/activateEmail.html', context)
			to_email = userMail
			send_mail(mail_subject, message, emailData["fromMailAddr"], [to_email])


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


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
	

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		form.base_fields['username'].label = 'Email'
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
		elif form.error_messages['inactive']:
			messages.error(request,"Bitte aktiviere deinen Account.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	form.base_fields['username'].label = 'Email'
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



