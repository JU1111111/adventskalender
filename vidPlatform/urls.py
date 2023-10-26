from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
	path("info", views.infoView, name="ifo"),
    path("<int:dateentry_id>/", views.detail, name="detail"),
]