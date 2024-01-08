import argparse
from playlist import create_playlist_from_source

def main():
    """
    Extracts args from command line and run script
    """
    # Create command line arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-s",
        "--source_playlist",
        help="The name of the playlist that contains the wanted content.",
        type=str,
        required=True,
    )
    arg_parser.add_argument(
        "-d",
        "--dest_playlist",
        help="The name of the output playlist",
        type=str,
        required=True,
    )
    arg_parser.add_argument(
        "-n",
        "--number_of_tracks_per_artist",
        help="Number of tracks to add per artist to new playlist from source playlist",
        type=int,
        default=5,
    )
    args = arg_parser.parse_args()

    create_playlist_from_source(
        args.source_playlist, args.dest_playlist, args.number_of_tracks_per_artist
    )


if __name__ == "__main__":
    main()
