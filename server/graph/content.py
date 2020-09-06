from server.graph.auth import get_token
from server.graph.requests import get_item, get_thumbnails
from server.common.caching import release_cache_thumbnail


def get_track_download_url(track):
    token = get_token(track.user)
    item = get_item(token, track.provider_id)
    return item.get('@microsoft.graph.downloadUrl')



def get_release_thumbnail_url(release, force=False):
    if not force and release.thumbnail:
        return release.thumbnail

    token = get_token(release.user)

    thumbs = get_thumbnails(token, release.provider_id).get('value', [])
    graph_url = thumbs[0]['medium']['url'] if thumbs else None

    if not graph_url:
        return ""

    return release_cache_thumbnail(release, graph_url)


def get_track_thumbnail_url(track, force=False):
    if not force and track.thumbnail:
        return track.thumbnail

    token = get_token(track.user)
    item = get_item(token, track.provider_id, select=('parentReference',))

    parent_id = item['parentReference']['id']
    thumbs = get_thumbnails(token, parent_id).get('value', [])
    graph_url = thumbs[0]['medium']['url'] if thumbs else None

    if not graph_url:
        return ""

    return release_cache_thumbnail(track.release, graph_url)
