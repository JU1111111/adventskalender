from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm

def secure(request):
    if request.user.is_authenticated:
        return redirect('/advent')
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("passwd") == "Adv3ntskal3nd3r!":
                response = HttpResponseRedirect("/login")
                response.set_cookie("seccookie","QWR2M250c2thbDNuZDNyIQ==")
                return response
            return render(request, template_name="secure.html", context={"msg":"Passwort ist falsch"})
    return render(request, template_name="secure.html")