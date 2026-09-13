from twilio.rest import Client
import smtplib
from config import account_sid,auth_token,my_email,my_password,from_number,to_number
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid =account_sid
        self.auth_token =auth_token
        self.my_email =my_email
        self.my_password =my_password
    def send_msg(self,msg):
        client = Client(self.account_sid, self.auth_token)
        message_1 = client.messages.create(
            body=f"{msg}",
            from_=from_number,
            to=to_number
        )
    def send_email(self,email,name,message):
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.my_password)
            connection.sendmail(from_addr=self.my_email,to_addrs=email,msg=message)
            connection.close()