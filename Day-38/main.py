import requests
import datetime as dt
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("API_KEY","Api key is not found")
app_id=os.environ.get("APP_ID","api id is not found")
nut_url=os.getenv("NUT_URL","A problem with nutritional endpoint")
sheety_endpoint=os.getenv("SHEETY_ENDPOINT","problem with sheety endpoint")
TOKEN=os.getenv("AUTH_TOKEN","error occured -A problem with token")
user_name=os.getenv("USER_NAME","no Username")
password=os.getenv("PASSWORD","no password")
basic=HTTPBasicAuth(user_name,password)
headers={
    "x-app-id":app_id,
    "x-app-key":api_key,
}
date=dt.datetime.now().date()
time=dt.datetime.now().time()
ques={
    "query":input("Tell The Exercise you did Today?--").title()
}
response_nut=requests.post(url=f"{nut_url}/v1/nutrition/natural/exercise",json=ques,headers=headers)
data=response_nut.json()
print(data)
exercise=data["exercises"][0]["name"]
duration=data["exercises"][0]["duration_min"]
calories=data["exercises"][0]["nf_calories"]
print(response_nut.text)
data={
    "sheet1":{
        "date":date.strftime("%d/%m/%Y"),
        "time":time.strftime("%H:%M:%S"),
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}
headers_auth={
"Authorization":f"Basic {TOKEN}"
}
response=requests.post(url=sheety_endpoint,json=data,headers=headers_auth)
print(response.text)
