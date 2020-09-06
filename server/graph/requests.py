from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
    graph_client = OAuth2Session(token=token)
    user = graph_client.get(f'{graph_url}/me')
    return user.json()


def get_children(token, driveitem_id):
    graph_client = OAuth2Session(token=token)
    url = f'{graph_url}/me/drive/items/{driveitem_id}/children?select=id,name,audio,file,folder'
    children = graph_client.get(url)
    return children.json()


def get_music_children(token):
    graph_client = OAuth2Session(token=token)
    url = f'{graph_url}/me/drive/special/music/children?select=id,name,audio,file,folder'
    children = graph_client.get(url)
    return children.json()


def get_item(token, driveitem_id, select=()):
    query_str = f"?select={','.join(select)}" if select else ""
    graph_client = OAuth2Session(token=token)
    url = f'{graph_url}/me/drive/items/{driveitem_id}{query_str}'
    item = graph_client.get(url)
    return item.json()


def get_thumbnails(token, driveitem_id):
    graph_client = OAuth2Session(token=token)
    url = f'{graph_url}/me/drive/items/{driveitem_id}/thumbnails'
    thumbs = graph_client.get(url)
    return thumbs.json()
