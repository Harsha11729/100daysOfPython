#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from joblib import expires_after

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from dotenv import load_dotenv
import requests_cache
requests_cache.install_cache("Flight_cache",expires_after=3600)
load_dotenv()
details=DataManager()
flight=FlightSearch()
flightdata = FlightData()
response_data=details.get_email()['formResponses1']
data=details.get_data()["sheet1"]
for response in response_data:
    print(response)
    email = response["email"]
    name = response["firstName"]

    for row in data:
        dept_id=row["depId"]
        arrive_id=row["arrId"]
        date=row["date"]
        price=row["price"]
        flightsearch=flight.flight_search(dept_id,arrive_id,date,1)
        print("searching for the direct flights")
        if not flightsearch:
            print("No direct flights are found.... searching for the indirect flights...............")
            flightsearch = flight.flight_search(dept_id, arrive_id, date, 0)
        flight_data=flightdata.find_cheapest_flights(flightsearch)
        print(flight_data)
        notification_manager=NotificationManager()
        if price>=flight_data["price"]:
            # send_msg=notification_manager.send_msg(f"You got best flight deal from {flight_data["departure"]} to {arrive_id} for {flight_data['price']}")
            send_email = notification_manager.send_email(email, name,f""" Subject:Alert::{flight_data["airline"]} has Great Deal for you...\n\n
             Hi {name},\n\n
             You got best flight deal on {flight_data["airline"]}
             from :{flight_data["departure"]} to {arrive_id} 
            for just {flight_data['price']}!  """)
