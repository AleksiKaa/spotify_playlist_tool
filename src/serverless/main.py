import functions_framework
from local.playlist import create_playlist_from_source


@functions_framework.http
def create_gym_playlist():
    """
    Creates a playlist with hardcoded values via http get request.
    """
    create_playlist_from_source("salimatsku", "sali", 5)
    return 200


@functions_framework.http
def create_gym_playlist_from_args(request):
    """
    Create a playlist with args from request body.
    """
    request_json = request.get_json(silent=True)
    source = request_json["source"]
    dest = request_json["dest"]
    num = request_json["num"]

    create_playlist_from_source(source, dest, num or 5)
    return 200

