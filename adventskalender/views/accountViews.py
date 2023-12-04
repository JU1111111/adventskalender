from django.shortcuts import  render, redirect
from adventskalender.forms import LoginForm
from adminDash.funtions.dbMod import getNumberOfCorrectVotes, getNumberOfIncorrectVotes, getNumberOfTotalVotes, getUserPlacement
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from adventskalender.tokens import account_activation_token
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.contrib import messages


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
        return HttpResponse('Vielen Dank für die E-Mail-Bestätigung. Das Konto ist nun freigeschaltet.')
    else:
        return HttpResponse('Der Aktivierungscode ist ungültig!')
	

def login_request(request):
	if request.user.is_authenticated:
		return redirect('/advent')
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		user = authenticate(username=form.data.get("username"), password=form.data.get("password"))
		if user is None:
			messages.error(request, "Die Email oder das Passwort ist falsch")
		elif form.is_valid():
				login(request, user)
				if user.last_login == None:
					return redirect("/info/")
				else:
					return redirect("/advent/")
		else:
			messages.error(request, "Bitte aktiviere dein Konto")
	form = LoginForm()
	return render(request=request, template_name="adventskalender/loginPage.html", context={"login_form":form})



def logout_request(request):
	logout(request)
	messages.info(request, "Du hast dich erfolgreich abgemeldet") 
	return redirect("/advent")


@login_required
def account(request):
	return render(request,"adventskalender/accountPage.html",{
		"placement":str(getUserPlacement(request.user.username)),
		"total":str(getNumberOfTotalVotes(request.user)),
		"right":str(getNumberOfCorrectVotes(request.user)),
		"wrong":str(getNumberOfIncorrectVotes(request.user))
		})


@login_required
def delAccount(request, confirm_commit):
	if confirm_commit == "True":
		request.user.delete()
		messages.add_message(request,messages.SUCCESS, "Dein Konto wurde erfolgreich gelöscht")
		return redirect('/')
	elif confirm_commit == "False":
		return render(request,"adventskalender/confirmDelete.html")