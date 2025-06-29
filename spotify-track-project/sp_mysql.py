
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import re
import mysql.connector


#Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='060580f491784cbf8c2b7a500e4d7684',
    client_secret='db428ba685e3456faaebd5ff82b0076f'
))

#DB
data_base = {
            "host" : "localhost",
            "user" : "root",
            "password": "Logeswar14",
            "database": "spotify"
}
# connect to the database
connection = mysql.connector.connect(**data_base)
cursor = connection.cursor()

#Trackurl
track_url = 'https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B'

# using regex  to extract track id
track_id = re.search( r'track/([a-zA-Z0-9]+)',track_url).group(1)

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
#Insert Data into Mysql
inser_query = '''
INSERT INTO track_data (track_name,artist,album,popularity,duration_min) 
VALUES (%s,%s,%s,%s,%s)
'''
cursor.execute(inser_query,(
    track_data["Track Name"],
    track_data["Artist"],
    track_data["Album"],
    track_data["Popularity"],
    track_data["Duration (minutes) "]
))
connection.commit()

print(f"track {track_data["Track Name"]} and all other inserted sucessfully.")
cursor.close()
connection.close()