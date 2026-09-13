import requests
from config import api_key,post_sheety_url,get_email_url,get_sheety_url
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_key=api_key
        self.post_sheety_url=post_sheety_url
        self.get_sheety_url=get_sheety_url
        self.get_email_url=get_email_url
    def post_data(self,dept_id:str,arr_id:str,date:str):
        data={
            "sheet1":{
                "depId":dept_id,
                "arrId":arr_id,
                "date":date            }
        }
        post_response=requests.post(url=self.post_sheety_url,json=data)
        print(post_response.status_code,post_response.text)
    def get_data(self):
        get_response=requests.get(url=self.get_sheety_url)
        get_response_data=get_response.json()
        return get_response_data
    def get_email(self):
        get_email_response=requests.get(url=self.get_email_url)
        get_email_data=get_email_response.json()
        return get_email_data

