from providers.graph.auth import get_token
from providers.graph.requests import get_item, get_thumbnails
from providers.common.caching import track_cache_thumbnail


def get_download_url(track):
    token = get_token(track.user)
    item = get_item(token, track.provider_id)
    return item.get('@microsoft.graph.downloadUrl')


def get_thumbnail_url(track):
    if track.thumbnail:
        return track.thumbnail

    token = get_token(track.user)
    item = get_item(token, track.provider_id, select=('parentReference',))

    parent_id = item['parentReference']['id']
    thumbs = get_thumbnails(token, parent_id).get('value', [])
    graph_url = thumbs[0]['medium']['url'] if thumbs else None

    return track_cache_thumbnail(track, graph_url)
