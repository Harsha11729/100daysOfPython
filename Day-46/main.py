import requests
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date_str=input("Enter the date of the songs you want YYYY-MM-DD:")
date=datetime.strptime(date_str,"%Y-%m-%d").date()
print(type(date))
url=f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
response=requests.get(url)
html=response.text
# print(html)
soup=BeautifulSoup(html,"html.parser")
tag=soup.find_all(name="h3",class_="chart-entry__title")
song_names=[tags.text for tags in tag]
with open("Top 100 songs.txt","w") as file:
    for song_name in song_names:
        file.write(f"{song_name}\n")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="bc313424ce9f4dcfabdd09573f208a32",
                                               client_secret="f40588ae7f104ed390205b14c66d9a6b",
                                               redirect_uri="http://127.0.0.1:8888/callback",
                                               scope="playlist-modify-private"))
song_uris=[]
playlist=sp.current_user_playlist_create(name="Madhuram's",description="My project",public=False)
with open("Top 100 songs.txt") as file:
    content=file.readlines()
    for song_name in content:
        song_name=song_name.strip()
        results = sp.search(q=song_name,limit=1)
        try:
            uri = results["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song_name} doesn't exist in Spotify")
sp.playlist_add_items(
            playlist_id=playlist["id"],
            items=song_uris
        )
print("playlist created Successfully")
print(f"playlist{playlist["id"]}")