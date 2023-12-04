from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def admin_check(user):
    return user.is_superuser


# Create your views here.
@login_required
@user_passes_test(admin_check)
def index(request):
	return render(request, "adminDash/index.html",)