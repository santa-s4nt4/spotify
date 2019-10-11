import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

mbg = 'spotify:artist:61VIpi1GmB7bTL3DCGWSlm'

client_id = 'fb2f486b467a4051b6a7810288e6a22a'
client_secret = 'b0d624bd8ddf407c979561d8950ad957'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(mbg)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
