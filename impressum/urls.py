from django.urls import path

from . import views

urlpatterns = [
    path("", views.impressum, name="impressum")
]