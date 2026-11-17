import requests
from bs4 import BeautifulSoup
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,"html.parser")
article_tag=soup.find_all(name='a',class_="storylink")
article_text=[tag.text for tag in article_tag]
article_link=[tag.attrs['href'] for tag in article_tag]
article_upvote=[score.text.split(" ") [0]for score in soup.find_all(name="span",class_="score")]
print(article_tag)
print(article_text)
print(article_link)
print(article_upvote)
maximum=max(article_upvote)
index=article_upvote.index(maximum)
print(article_text[index])
print(article_link[index])
print(article_upvote[index])