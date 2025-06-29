import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
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

#read track url
filepath = "tracks.csv"
with open(filepath,'r') as file:
    track_urls = file.readlines()

# process each url
for track_url in track_urls:
    track_url = track_url.strip()
    try:

        track_id = re.search( r'track/([a-zA-Z0-9]+)',track_url).group(1)


        track= sp.track(track_id)


        track_data = {
            "Track Name" : track["name"],
            "Artist" : track['artists'][0]['name'],
            'Album' : track['album']['name'],
            "Popularity": track['popularity'],
            "Duration (min)": track['duration_ms'] / 60000
        }

        inset_query = '''
        INSERT INTO track_data (track_name, artist, album , popularity, duration_min)
        VALUES (%s,%s,%s,%s,%s)
        '''
        cursor.execute(inset_query,(
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (min)']

        ))
        connection.commit()
        print(f"inserted: {track_data["Track Name"]}  by {track_data['Artist']}")
    except Exception as e :
        print(f"Error processing URL: {track_url}, Error {e}")
cursor.close()
connection.close()

print("All tracks have been processed and inserted into the database.")