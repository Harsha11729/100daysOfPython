import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()
url_endpoint=os.getenv("url_endpoint")
TOKEN=os.getenv("TOKEN")
USER_NAME=os.getenv("USER_NAME")
parameters={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=url_endpoint,json=parameters)
graph_endpoint=f"{url_endpoint}/{USER_NAME}/graphs"
graph_id="graph1"
graph_config={
    "id":graph_id,
    "name":"Streak",
    "unit":"commit",
    "type":"int",
    "color":"ichou"
}
headers={
    "X-USER-TOKEN":TOKEN
}
date=dt.datetime.now().date()
today=date.strftime("%Y%m%d")
print(today)
pixel_data={
    "date":'20260601',
    "quantity":"8"
}

graph_response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(graph_response.text)
graph_data_send_endpoint=f"https://pixe.la/v1/users/{USER_NAME}/graphs/{graph_id}"
data_req_response=requests.put(url=f"{graph_data_send_endpoint}",json=pixel_data,headers=headers)
print(data_req_response.text)
delete_graph_req=requests.delete(f"https://pixe.la/v1/users/{USER_NAME}/graphs/{graph_id}/20260601",json=pixel_data,headers=headers)
print(delete_graph_req.text)