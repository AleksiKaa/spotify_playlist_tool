# spotify_playlist_tool

## Environment variables

.env variables needed:

- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URL
- SPOTIFY_USER_ID

## Usage

Script is used with command

```bash
python main.py -s "string" -d "string" -n "integer"
```

, where -s is the name of the source playlist, -d the name of the destination playlist, and -n the number of tracks to add per artist to the destination playlist.
