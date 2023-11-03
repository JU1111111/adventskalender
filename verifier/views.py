from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth import get_user_model

from.forms import NewStudentForm, NewUserForm
from .tokens import account_activation_token
from .decorators import user_not_authenticated

#@user_not_authenticated
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)#Form for email, PW
		form2 = NewStudentForm(request.POST)#Form for class / year
		
		if form.is_valid():
			userMail = form.cleaned_data.get('email')
			username = userMail.replace('.',' ').split('@')[0]
			user = form.save(commit=False)
			#setting username and first/last name
			user.username = username
			user.last_name = username.split(' ')[-1]
			firstName = ''
			for name in username.split(' ')[:-1]:
				firstName += f' {name}'
			user.first_name = firstName

			user.is_active = False #active to false for verification
			user.save()
			student = form2.save(commit=False)
			student.user = user
			student.save() #save student for class and year


			activateEmail(request, user, form.cleaned_data.get('email'))
			return redirect('login')

		else:
			for error in list(form.errors.values()):
				messages.error(request, error)

	else:
		form = NewUserForm()
		form2 = NewStudentForm

	return render(
		request=request,
		template_name="adventskalender/regPage.html",
		context={"register_form":form, 
		   "registerStudent_form":form2}
		)



def activateEmail(request, user, to_email):
	mail_subject = 'Activate your user account.'
	message = render_to_string('verifier/activateEmailTemplate.html', {
		'user': user.username,
		'domain': get_current_site(request).domain,
		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		'token': account_activation_token.make_token(user),
		'protocol': 'https' if request.is_secure() else 'http'
	})
	email = EmailMessage(mail_subject, message, to=[to_email])
	if email.send():
		messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
			received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
	else:
		messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid! ')
    
    return redirect('login')


def notActive(request):
	return render(request, 'verifier/notActivated.html')