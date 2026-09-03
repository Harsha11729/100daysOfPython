# import smtplib as smtp
# my_email=""
# password=""
# connection=smtp.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs=" ",msg="Hello , This is Harsha")
# connection.close()

# import datetime as dt
# now=dt.datetime.now()
# print(now)
# print(now.month)
# print(now.weekday())

# import datetime as dt
# import random
# now=dt.datetime.now()
# curr_day=now.weekday()
# with open("quotes.txt") as file:
#     quotes=file.readlines()
# quote=random.choice(quotes)
# import smtplib as smtp
# my_email="harsha.kandepu05@gmail.com"
# password="fyjemkkgpakrmikp"
# with smtp.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     if curr_day==3:
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="",
#             msg=quote
#         )
