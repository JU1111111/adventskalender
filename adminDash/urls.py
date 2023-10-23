from django.urls import path
from django.contrib.auth.decorators import user_passes_test

from . import views

urlpatterns = [
    path("", views.index, name="index"),
	path("database", views.database, name="database"),
	path("database/addDaysToDB", views.addDaysToDB, name="addDaysToDB"),
	path("database/importDB", views.importFromDoc, name="importFromDoc")

]