import requests
from bs4 import BeautifulSoup
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_text=response.text
soup=BeautifulSoup(html_text,"html.parser")
title=soup.find_all(name="h3",class_="title")
titles=list(reversed([name.text for name in title]))
with open("Top 100 movies.txt","w",encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")