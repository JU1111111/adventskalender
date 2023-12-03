from django.urls import path, include 
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.register, name='register'),
	path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(template_name="verifier/templates/registration/password_reset_form.html"),
    ),
	path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="verifier/templates/registration/password_reset_done.html"),
    ),
	path(
        "/accounts/reset/Nw/set-password/",
        auth_views.PasswordResetConfirmView.as_view(template_name="verifier/templates/registration/password_reset_confirm.html"),
    ),
	path('accounts/', include("django.contrib.auth.urls"), name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
	path('NotActive', views.notActive, name='notActivate'),
	
]