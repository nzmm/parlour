from celery import shared_task
from server.graph.auth import PROVIDER_GRAPH
from server.graph import sync as graph_sync


@shared_task(ignore_result=True)
def sync_music_task(user, provider):
    if not user or not provider:
        return
    if provider == PROVIDER_GRAPH:
        graph_sync.sync_music(user)
    return


@shared_task(ignore_result=True)
def sync_thumbs_task(user, provider):
    if not user or not provider:
        return
    if provider == PROVIDER_GRAPH:
        graph_sync.sync_thumbnails(user)
    return
