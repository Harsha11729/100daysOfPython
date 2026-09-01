import requests
import datetime
import smtplib as smtp
import time
my_latitude=17.4922132
my_longitude=-78.4066366
my_email=""
my_password=''
parameters={
    "lat":my_latitude,
    "lng":my_longitude,
    "formatted":0
}
response=requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()
iss_latitude=float(data['iss_position']['latitude'])
iss_longitude=float(data['iss_position']['longitude'])
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset=int(data['results']['sunset'].split('T')[1].split(':')[0])
now=datetime.datetime.now()
while True:
    time.sleep(60)
    if my_latitude-5<=iss_latitude<=my_latitude+5 and my_longitude-5<=iss_longitude<=my_longitude+5 and (now.hour<=sunrise or now.hour>=sunset):
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="ISS(international space station) is above you . Look up!")
