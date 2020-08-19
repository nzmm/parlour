from providers.graph.auth import get_token
from providers.graph.requests import get_music_children


def handle_folder(item):
    return


def handle_file(item):
    return


def sync_music(user):
    token = get_token(user)
    music = get_music_children(token)

    for item in music.get('value', []):
        print(item)
    return
