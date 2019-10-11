import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

client_id = 'fb2f486b467a4051b6a7810288e6a22a'
client_secret = 'b0d624bd8ddf407c979561d8950ad957'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.audio_features('6dnPQD7riP9K0ub8tbFJV5')
pprint.pprint(result)
