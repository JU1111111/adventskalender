from django.shortcuts import  render
from django.contrib.auth.decorators import login_required


@login_required
def infoView(request):
	return render(request, "adventskalender/infoPage.html")

@login_required
def impressumView(request):
	return render(request, "adventskalender/impressum.html")

@login_required
def privacyNoticeView(request):
	return render(request, "adventskalender/datenschutz.html")


