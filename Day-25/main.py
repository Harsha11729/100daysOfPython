# import csv
# with open("weather_data.csv") as file:
#     content = csv.reader(file)
#     temperatures = []
#     for row in content:
#         temperatures.append(row[1])
#     print(temperatures)
# import pandas
# data=pandas.read_csv("weather_data.csv")
# # temp=data['temp'].to_list()
# # print(data['temp'].max())
# # avg=sum(temp)/len(temp)
# # print(avg)
# # print(data[data.day=='Monday'])
# # print(data[data.temp==data.temp.max()])
# monday=data[data.day=='Monday']
# mon_temp=monday.temp
# mon_fa=mon_temp*(9/5)+32
# print(mon_fa)
import pandas as pd
with open('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260310.csv') as data:
    content=pd.read_csv(data)
    colors_len1=len(content[content['Primary Fur Color']=='Gray'])
    colors_len2=len(content[content['Primary Fur Color']=='Cinnamon'])
    colors_len3=len(content[content['Primary Fur Color']=='Black'])
    data={
        "Primary Fur Color":["Gray","Cinnamon","Black"],
        "Color":[colors_len1,colors_len2,colors_len3]
    }
    df=pd.DataFrame(data)
    df.to_csv("Squerrals_count_colours.csv")
    print(colors_len1,colors_len2,colors_len3)
    print(content['Primary Fur Color'].value_counts())