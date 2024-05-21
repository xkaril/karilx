from __future__ import print_function
import datetime
import os.path
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_event():
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    event = {
      'summary': 'Cita Médica',
      'location': 'Clínica Ejemplo',
      'description': 'Consulta médica general.',
      'start': {
        'dateTime': '2024-06-15T10:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2024-06-15T11:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'attendees': [
        {'email': 'paciente@example.com'},
      ],
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Evento creado: %s' % (event.get('htmlLink')))

create_event()
