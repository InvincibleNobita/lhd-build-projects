import os
from twilio.rest import Client


account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)

client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                      to=os.environ.get('PHONE_NUMBER'),
                      body='Hello buddy! Its working properly!')