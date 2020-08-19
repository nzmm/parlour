from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
    graph_client = OAuth2Session(token=token)
    user = graph_client.get(f'{graph_url}/me')
    return user.json()


def get_albums(token):
    graph_client = OAuth2Session(token=token)
    songs = graph_client.get(f'{graph_url}/me/drive/special/music/children?expand=thumbnails&select=id,name,thumbnails')
    return songs.json()


def get_music_children(token):
    graph_client = OAuth2Session(token=token)
    children = graph_client.get(f'{graph_url}/me/drive/special/music/children?expand=thumbnails&select=id,name,thumbnails,audio,file,folder')
    return children.json()
