from django.shortcuts import render, redirect

# Create your views here.
def impressum(request):
    if request.method == "GET" and request.COOKIES.get('seccookie') != "QWR2M250c2thbDNuZDNyIQ==":
        return redirect('/secure')
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, template_name="impressum.html")