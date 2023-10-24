from datetime import timedelta
from vidPlatform.models import DateEntry, Choice, Vote
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1oGrpsrnZnyuF8eBdKHlUTh7NrN4tpqIvNZEPlD6UPQM'
SAMPLE_RANGE_NAME = 'A2:J'

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
                'C:\\Users\\Julian\\Desktop\\advendskalenderDjango\\adventskalender\\adminDash\\credentials.json', SCOPES)
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
                continue
            entry = DateEntry(title=row[1], pub_date='2023-12-'+row[0]+' 00:20:0', start_date='2023-12-'+row[0], end_date='2023-12-'+str(int(row[0])+1), videoLink=row[2], resolutionVidLink=row[3], question=row[6])
            entry.save()
            r_answer = Choice(question=entry, choice_text=row[7], isCorrect=True, votes=0)
            w_answer1 = Choice(question=entry, choice_text=row[8], isCorrect=False, votes=0)
            w_answer2 = Choice(question=entry, choice_text=row[9], isCorrect=False, votes=0)
            w_answer3 = Choice(question=entry, choice_text=row[10], isCorrect=False, votes=0)
            r_answer.save()
            w_answer1.save()
            w_answer2.save()
            w_answer3.save()
            # DataEntry.create(day, title, videoid, solutionid, authors, question, r_answer, w_answers)
            #entries.append(DataEntry.create(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]]))
            #print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]])
    except HttpError as err:
        print(err)
