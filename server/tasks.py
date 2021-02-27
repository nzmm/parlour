from celery import shared_task
from django.contrib.auth.models import User
from server.models import Token
from server.graph.auth import PROVIDER_GRAPH
from server.graph import sync as graph_sync


@shared_task(ignore_result=True)
def sync_music_task(user_id, provider_id):
    user = User.objects.get(pk=user_id)
    token = Token.objects.get(pk=provider_id)
    if token.provider == PROVIDER_GRAPH:
        graph_sync.sync_music(user)
    return


@shared_task(ignore_result=True)
def sync_thumbs_task(user_id, provider_id):
    user = User.objects.get(pk=user_id)
    token = Token.objects.get(pk=provider_id)
    if token.provider == PROVIDER_GRAPH:
        graph_sync.sync_thumbnails(user)
    return
