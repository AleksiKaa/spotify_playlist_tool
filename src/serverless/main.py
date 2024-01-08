import functions_framework
import json

from local.playlist import create_playlist_from_source


@functions_framework.http
def create_gym_playlist(request):
    """
    Creates a playlist with hardcoded values via http get request.
    """

    result = create_playlist_from_source(source="salimatsku", dest="sali", num=5)
    data = {"status": result}
    if result == "success":
        return json.dumps(data), 200
    return json.dumps(data), 400


@functions_framework.http
def create_gym_playlist_from_args(request):
    """
    Create a playlist with args from request body.
    """
    request_json = request.get_json(silent=True)
    source = request_json["source"]
    dest = request_json["dest"]
    num = request_json["num"]

    result = create_playlist_from_source(source=source, dest=dest, num=num)
    data = {"status": result}
    if result == "success":
        return json.dumps(data), 200
    return json.dumps(data), 400
