import requests
from serpapi import account
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid=os.getenv('account_sid')
auth_token=os.getenv('auth_token')
parameters={
    # 'LAT':17.469333,
    # 'LON':78.367931,
    'lat':17.469333,
    'lon':78.367931,
    # 'appid':'66430b0029a234df20844bb38f2004b1',
    'appid':os.getenv('appid'),
    'units':'metric'
}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
print(response.status_code)
data=response.json()
will_rain=False
for i in range(len(data['list'])):
    id=data['list'][i]['weather'][0]['id']
    if id<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring umbrella today ☔",
        from_=os.getenv('from_ph'),
        to=os.getenv('to_ph')
    )
    print(message.sid)
