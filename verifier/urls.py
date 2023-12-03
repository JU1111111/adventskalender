from django.urls import path, include 
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.register, name='register'),
	path('accounts/', include("django.contrib.auth.urls"), name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
	path('NotActive', views.notActive, name='notActivate'),
	
]
