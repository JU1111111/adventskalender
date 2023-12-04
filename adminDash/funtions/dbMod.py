from datetime import timedelta
import datetime
from vidPlatform.models import DateEntry, Choice, Vote, Student
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.contrib.auth import get_user_model
from adminDash.models import CorrectUserVotes
from django.contrib.auth import get_user_model

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1oGrpsrnZnyuF8eBdKHlUTh7NrN4tpqIvNZEPlD6UPQM'
SAMPLE_RANGE_NAME = 'A2:L'

UserModel = get_user_model()


def changeDateOfAllEntries(DaysToAdd):
	timeDelt = timedelta(days=DaysToAdd)
	entries = DateEntry.objects.all()

	for entry in entries:
		entry.start_date += timeDelt
		entry.end_date += timeDelt
		entry.save()


def getDateEntries():
	alllentries = DateEntry.objects.all()
	alllentries.delete()
	# Authentication
	creds = None
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'./adminDash/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		with open('token.json', 'w') as token:
			token.write(creds.to_json())

	try:
		service = build('sheets', 'v4', credentials=creds)
		sheet = service.spreadsheets()
		result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
									range=SAMPLE_RANGE_NAME).execute()
		values = result.get('values', [])
		if not values:
			print('No data found.')
			return
		#Code
		for row in values:
			if len(row) < 10 or "" in row:
				print(len(row))
				continue
			entry = DateEntry(title=row[1], pub_date=datetime.datetime.now(), start_date='2023-12-'+row[0], end_date='2023-12-'+str(int(row[0])+1), videoLink=row[2], resolutionVidLink=row[3], question=row[7])
			entry.save()
			r_answer = Choice(question=entry, choice_text=row[8], isCorrect=True, votes=0)
			w_answer1 = Choice(question=entry, choice_text=row[9], isCorrect=False, votes=0)
			w_answer2 = Choice(question=entry, choice_text=row[10], isCorrect=False, votes=0)
			w_answer3 = Choice(question=entry, choice_text=row[11], isCorrect=False, votes=0)
			r_answer.save()
			w_answer1.save()
			w_answer2.save()
			w_answer3.save()
			# DataEntry.create(day, title, videoid, solutionid, authors, question, r_answer, w_answers)
			#entries.append(DataEntry.create(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]]))
			#print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]])
	except HttpError as err:
		print(err)


	

def refreshWinnersUpToYesterday():

	todaysDay = datetime.date.today()
	currentCorrects = CorrectUserVotes.objects.all().delete()

	allUsers = UserModel.objects.filter()

	numOfCorrects = {}
	for user in allUsers:
		NumOfRightVotes = Vote.objects.filter(choice__isCorrect=True, author=user, choice__question__end_date__lte=datetime.datetime.today()).count()
		numOfCorrects[user.get_username()] = NumOfRightVotes

		correctVotesDBEntry = CorrectUserVotes(user=user,
										 correctVotesNumber = NumOfRightVotes, 
										 currentPlacement=0, 
										 lastRefresh = datetime.date.today() - datetime.timedelta(days=1))
		
		if user.first_name != '' and user.last_name != '': 
			firstNamesSplit = user.first_name.split(' ')
			correctVotesDBEntry.displayName = firstNamesSplit[1].capitalize() + " " + user.last_name[0].upper() + ". "
			correctVotesDBEntry.isStudent = True
		else:
			correctVotesDBEntry.isStudent = False
			correctVotesDBEntry.displayName = "User Number " + str(user.id)

		correctVotesDBEntry.save()

	FiveToEightCorrectVotes = CorrectUserVotes.objects.filter(user__student__studentYear__in=range(5,9)).order_by("-correctVotesNumber")
	place = 0
	previousnumberOfVotes = 0

	for rightVotes in FiveToEightCorrectVotes:
		if rightVotes.isStudent:
			if rightVotes.correctVotesNumber == previousnumberOfVotes:
				rightVotes.currentPlacement = place
			else:
				place += 1
				rightVotes.currentPlacement = place
				previousnumberOfVotes = rightVotes.correctVotesNumber

		elif not rightVotes.isStudent:
			if rightVotes.correctVotesNumber == previousnumberOfVotes:
				rightVotes.currentPlacement = place 
			else:
				rightVotes.currentPlacement = place + 1
				
		rightVotes.lastRefresh = todaysDay
		rightVotes.save()
	

	NineToThirteenCorrectVotes = CorrectUserVotes.objects.filter(user__student__studentYear__in=range(9,14)).order_by("-correctVotesNumber")
	place = 0
	previousnumberOfVotes = 0
	for rightVotes in NineToThirteenCorrectVotes:
		if rightVotes.isStudent:
			if rightVotes.correctVotesNumber == previousnumberOfVotes:
				rightVotes.currentPlacement = place
			else:
				place += 1
				rightVotes.currentPlacement = place
				previousnumberOfVotes = rightVotes.correctVotesNumber

		elif not rightVotes.isStudent:
			if rightVotes.correctVotesNumber == previousnumberOfVotes:
				rightVotes.currentPlacement = place 
			else:
				rightVotes.currentPlacement = place + 1


		rightVotes.lastRefresh = todaysDay
		rightVotes.save()
		
	return numOfCorrects


def getCurrentWinners(years:[], forceRefresh=False):

	if forceRefresh:
		refreshWinnersUpToYesterday()
	
	winnerz = CorrectUserVotes.objects.filter(user__student__studentYear__in=years).order_by("-correctVotesNumber")[:10]

	winnerzObjects = []
	if not winnerz:
		refreshWinnersUpToYesterday()
		winnerz = CorrectUserVotes.objects.filter(user__student__studentYear__in=years).order_by("-correctVotesNumber")[:10]
		if not winnerz:
			return winnerzObjects
		
	if winnerz[0].lastRefresh != datetime.date.today():
		refreshWinnersUpToYesterday()

	place = 1
	for winner in winnerz:
		winnerzStudent = Student.objects.get(user=winner.user)
		winObj = Winner(winner.correctVotesNumber, winnerzStudent, winner.currentPlacement)
		winObj.isActualStudent = winner.isStudent
		winObj.displayName = winner.displayName
		winnerzObjects.append(winObj)

	return winnerzObjects


def getUserPlacement(username):
	user = UserModel.objects.get(username=username)

	try:
		studentOfUser = Student.objects.get(user=user)
	except:
		return "None"

	if studentOfUser.studentYear in range(5,9):
		years = range(5,9)
	elif studentOfUser.studentYear in range(9,13):
		years = range(9,14)

	correctUserVotes = CorrectUserVotes.objects.get(user=user)
	if correctUserVotes.lastRefresh != datetime.date.today() or not correctUserVotes:
		refreshWinnersUpToYesterday()

	placement = correctUserVotes.currentPlacement

	return placement


class Winner():
	def __init__(self, numOfRightVotes, student, placement):
		self.place = placement
		self.displayName = ''
		self.isActualStudent = False

		year = str(student.studentYear)
		self.klasse = year + student.studentClass
		self.rightVotes = numOfRightVotes


def getNumberOfTotalVotes(username):
	numberOfTotalVotes = Vote.objects.filter(author__username=username, choice__question__end_date__lte=datetime.date.today() + datetime.timedelta(days=1)).count()
	return numberOfTotalVotes


def getNumberOfCorrectVotes(username):
	numberOfCorrectVotes = Vote.objects.filter(author__username=username, choice__isCorrect=True, choice__question__end_date__lte=datetime.date.today()).count()
	return numberOfCorrectVotes

def getNumberOfIncorrectVotes(username):
	numberOfIncorrectVotes = Vote.objects.filter(author__username=username, choice__isCorrect=False, choice__question__end_date__lte=datetime.date.today()).count()
	return numberOfIncorrectVotes
