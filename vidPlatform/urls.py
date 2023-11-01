from django.urls import path

from .views import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:dateentry_id>/", views.detail, name="detail"),
]