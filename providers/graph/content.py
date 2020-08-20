from django.shortcuts import get_object_or_404
from providers.graph.auth import get_token
from providers.graph.requests import get_item, get_thumbnails
from providers.models import Track


def get_download_url(user, track_id):
    track = get_object_or_404(Track, pk=track_id, user=user)
    token = get_token(user)
    item = get_item(token, track.provider_id)
    return item.get('@microsoft.graph.downloadUrl')


def get_thumbnail_url(user, track_id):
    track = get_object_or_404(Track, pk=track_id, user=user)
    token = get_token(user)
    item = get_item(token, track.provider_id, select=('parentReference',))

    parent_id = item['parentReference']['id']
    thumbs = get_thumbnails(token, parent_id).get('value', [])
    return thumbs[0]['medium']['url'] if thumbs else None
