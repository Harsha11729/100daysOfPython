import os
from dotenv import load_dotenv
load_dotenv()
# data_manager
api_key=os.getenv("api_key")
post_sheety_url=os.getenv("post_sheety_url")
get_sheety_url=os.getenv("get_sheety_url")
get_email_url=os.getenv("get_email_url")

flight_search_api =os.getenv("flight_search_api")
flight_url = os.getenv("flight_url")
account_sid=os.getenv("account_sid")
auth_token=os.getenv("auth_token")
my_email=os.getenv("my_email")
my_password = os.getenv("my_password")
from_number=os.getenv("from_number")
to_number=os.getenv("to_number")
