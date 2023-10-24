from django.urls import path
from django.contrib.auth.decorators import user_passes_test

from . import views, databaseresponses

urlpatterns = [
    path("", views.index, name="index"),
	path("database", databaseresponses.database, name="database"),
	path("database/addDaysToDB", databaseresponses.addDaysToDB, name="addDaysToDB"),
	path("database/importDB", databaseresponses.importFromDoc, name="importFromDoc"),
	path("EmailTest", views.emailTest, name="emailTest"),
	path("EmailTestSend", views.emailTestSend, name="emailTestSend"),

]