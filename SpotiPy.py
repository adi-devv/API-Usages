import requests
from bs4 import BeautifulSoup

import SpotiPy, os
from SpotiPy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
time = input("Time travel to which year? [YYYY-MM-DD]")
resp = requests.get(f"https://www.billboard.com/charts/hot-100/{time}")

soup = BeautifulSoup(resp.text, 'html.parser')
songs = [h3.string.strip() for h3 in soup.select('li ul li h3')]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["Spotify_id"],
                                               client_secret=os.environ["Spotify_secret"],
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               username="Pithonn", ))
user_id = sp.current_user()["id"]

uris = []

for s in songs:
    res = sp.search(f"track:{s}", type="track")
    try:
        uri = res["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(s, 'not found.')
playlist = sp.user_playlist_create(user=user_id, name=f"Pithonn", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=uris)