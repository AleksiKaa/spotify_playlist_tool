import argparse

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Create command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument(
    "-p",
    "--playlist_name",
    help="The name of the playlist that contains the wanted content.",
    required=True,
)
argParser.add_argument(
    "-o", "--out_playlist", help="The name of the output playlist", required=True
)
args = argParser.parse_args()

# Load spotify credentials
load_dotenv()

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists = sp.current_user_playlists()
for item in playlists["items"]:
    if item["name"] == args.playlist_name:
        print(True)
    else:
        print(False)