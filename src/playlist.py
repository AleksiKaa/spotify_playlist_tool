import random
from collections import defaultdict
from os import getenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


def create_playlist_from_source(source, dest, num):
    """
    Creates a playlist with name dest for current user from tracks in source playlist
    """

    # Load spotify credentials
    load_dotenv()

    # Create spotipy client
    scope = ["user-library-read", "playlist-modify-public"]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Find the id of the argument playlist
    playlist_id = None
    playlists = sp.current_user_playlists()
    for playlist in playlists["items"]:
        if playlist["name"] == source:
            playlist_id = playlist["id"]
        if playlist["name"] == dest:
            print(f"A playlist named {dest} already exists!")
            return

    if playlist_id is None:
        print(f"No playlist named {source} exists for this user!")
        return

    # Create a new playlist with name dest
    print(f"Creating playlist {dest}")
    new_playlist = sp.user_playlist_create(user=getenv("SPOTIFY_USER_ID"), name=dest)
    print("Done.")

    # Store all tracks here
    track_store = defaultdict(list)

    # Get the length of the playlist
    playlist_len = sp.playlist_tracks(playlist_id=playlist_id, fields="total")["total"]
    offset = 0

    # Method returns 100 tracks at a time, iterate until all have been fetched
    print("Collecting tracks from source playlist...")
    while offset < playlist_len:
        print(f"Handling {offset}/{playlist_len}")
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
    print("Done.")

    print("Adding tracks to playlist...")
    for _, track_id_list in dict.items(track_store):
        subset = random.sample(track_id_list, min(len(track_id_list), num))

        sp.playlist_add_items(playlist_id=new_playlist["id"], items=subset)
    print("Done.")

    print(f"Playlist {dest} successfully created.")
    return
