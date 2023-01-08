from __future__ import print_function
from datetime import datetime,  timedelta
from datetime import date
from pytz import timezone 
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def event():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.now(timezone("Asia/Kolkata")).isoformat()
        end = (datetime.now(timezone("Asia/Kolkata")) + timedelta(hours=9)).isoformat()
        da = date.today()

        now = str(da) + "T05:00:00.457121+05:30"
        end = str(da) + "T23:00:00.457121+05:30"

        events_result = service.events().list(calendarId='primary', timeMin=now, timeMax = end, 
                                              singleEvents=True, timeZone='Asia/Kolkata',
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return 'No Event'

        main_allday = list()
        main_event_text = list()
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))

            start = start.split('T')[0]
            end = end.split('T')[0]
            if start == end:
                Allday = False
            else:
                Allday = True

            main_allday.append(str(Allday))

            main_event_text.append(str(event['summary'].lower()))
            print(start, end, Allday,  event['summary'])

        return  main_event_text, main_allday
        

    except HttpError as error:
        print('An error occurred: %s' % error)
        return 'An error occurred: %s' % error


if __name__ == '__main__':
    event()
    