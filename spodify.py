
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector


#Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='060580f491784cbf8c2b7a500e4d7684',
    client_secret='db428ba685e3456faaebd5ff82b0076f'
))



#Trackurl
track_url = 'https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B'

# using regex  to extract track id
track_id = re.search( r'track/([a-zA-z0-9]+)',track_url).group(1)

# Fetch track detail
track = sp.track(track_id)
print(track)
# Extract metadata
track_data ={
             "Track Name" : track['name'],
             "Artist": track['artists'][0]['name'],
             "Album": track['album']['name'],
             'Popularity': track['popularity'],
             'Duration (minutes) ': track['duration_ms'] /60000
}
#Display metadata
print(f"\n Track Name: {track_data['Track Name']}")
print(f"\n Artist Name:{track_data["Artist"]} ")
print(f"\n Album Name:{track_data["Album"]} ")
print(f"Popularity: {track_data["Popularity"]} ")
print(f"Duration: {track_data["Duration (minutes) "]} ")

# Converts metadata to DataFrame using pandas
df = pd.DataFrame([track_data])
print(f"\n Track data as DataFrame")
print(df)

# save MetaData as CSV
df.to_csv("spodify_trackdata.csv",index = False)

# Visulation using mat
features = ["Popularity", "Duration (minutes)"]
values  = [track_data["Popularity"], track_data["Duration (minutes) "]]

plt.figure(figsize=(8,5))
plt.bar(features,values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data["Track Name"]}'")
plt.ylabel('Value')
plt.show()