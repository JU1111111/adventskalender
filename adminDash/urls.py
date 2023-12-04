from django.urls import path

from .views import views, viewsDatabase, viewsEmail, viewsLeaderboard, viewsEntryCheck

urlpatterns = [
    path("", views.index, name="index"),
	path("database", viewsDatabase.database, name="database"),
	path("database/addDaysToDB", viewsDatabase.addDaysToDB, name="addDaysToDB"),
	path("database/importDB", viewsDatabase.importFromDoc, name="importFromDoc"),
	path("EmailTest", viewsEmail.emailTest, name="emailTest"),
	path("EmailTestSend", viewsEmail.emailTestSend, name="emailTestSend"),
	path("leaderboard", viewsLeaderboard.leaderboard, name="leaderboard"),
	path("EntryCheck", viewsEntryCheck.entryCheck, name="leaderboard"),

]