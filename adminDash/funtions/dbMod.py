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

	currentCorrects = CorrectUserVotes.objects.all().delete()

	allUsers = UserModel.objects.filter()

	numOfCorrects = {}
	for user in allUsers:
		NumOfRightVotes = Vote.objects.filter(choice__isCorrect=True, author=user, choice__question__end_date__lte=datetime.datetime.today()).count()
		numOfCorrects[user.get_username()] = NumOfRightVotes

		correctVotesDBEntry = CorrectUserVotes(user=user,correctVotesNumber = NumOfRightVotes)
		correctVotesDBEntry.save()

	return numOfCorrects



	


def getCurrentWinners(years:[], refresh=False):
	#numOfCorrect = refreshWinnersUpToYesterday()


	if refresh:
		refreshWinnersUpToYesterday()
	

	winnerz = CorrectUserVotes.objects.filter(user__student__studentYear__in=years).order_by("-correctVotesNumber")[:10]
	return winnerz
