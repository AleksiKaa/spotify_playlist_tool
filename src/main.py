import argparse
import random
from collections import defaultdict
from os import getenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Create command line arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-p",
    "--playlist_name",
    help="The name of the playlist that contains the wanted content.",
    required=True,
)
arg_parser.add_argument(
    "-o", "--out_playlist", help="The name of the output playlist", required=True
)
args = arg_parser.parse_args()

# Load spotify credentials
load_dotenv()

# Create spotipy client
scope = ["user-library-read", "playlist-modify-public"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Find the id of the argument playlist
playlist_id = None
playlists = sp.current_user_playlists()
for playlist in playlists["items"]:
    if playlist["name"] == args.playlist_name:
        playlist_id = playlist["id"]
    if playlist["name"] == args.out_playlist:
        raise Exception(f"A playlist named {args.out_playlist} already exists!")

if playlist_id is None:
    raise Exception(f"No playlist named {args.playlist_name} exists for this user!")

# Get the length of the playlist
playlist_len = sp.playlist_tracks(playlist_id=playlist_id, fields="total")["total"]
offset = 0

# Create a new playlist with argument name
new_playlist = sp.user_playlist_create(
    user=getenv("SPOTIFY_USER_ID"), name=args.out_playlist
)

print(new_playlist)

# Store all tracks here
track_store = defaultdict(list)

# Method returns 100 tracks at a time, iterate until all have been fetched
while offset < playlist_len:
    limit = 100
    next_tracks = sp.playlist_tracks(
        playlist_id=playlist_id,
        offset=offset,
        market="FI",
        limit=limit,
        fields=["items"],
    )["items"]
    offset += limit

    # Group store by artist id
    for t in next_tracks:
        artist_id = t["track"]["album"]["artists"][0]["id"]
        track_id = t["track"]["id"]
        track_store[artist_id].append(track_id)

# Add at most this number of tracks per artist to playlist
max_num_per_artist = 5

for _, track_id_list in dict.items(track_store):
    subset = random.sample(track_id_list, min(len(track_id_list), max_num_per_artist))

    sp.playlist_add_items(playlist_id=new_playlist["id"], items=subset)
