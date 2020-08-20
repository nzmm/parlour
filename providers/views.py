from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from providers.graph.auth import get_sign_in_url, get_token_from_code, get_token, store_token
from providers.common import queries
from providers.common import serializers
from providers.graph.content import get_download_url, get_thumbnail_url


def graph_sign_in(request):
    sign_in_url, state = get_sign_in_url()
    request.session['auth_state'] = state
    return HttpResponseRedirect(sign_in_url)


def graph_callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = get_token_from_code(request.get_full_path(), expected_state)
    store_token(request.user, token)
    return HttpResponseRedirect(reverse('home'))


def graph_sign_out(request):
    remove_token(request.user)
    return HttpResponseRedirect(reverse('home'))


def get_artists(request):
    artists = queries.get_artists_query(request.user)
    return JsonResponse({'artists': serializers.serialize_artists(artists)})


def get_albums(request):
    albums = queries.get_albums_query(request.user)
    return JsonResponse({'albums': serializers.serialize_albums(albums)})


def get_songs(request):
    songs = queries.get_songs_query(request.user)
    return JsonResponse({'songs': serializers.serialize_songs(songs)})


def get_download(request):
    track_id = request.GET.get('id')
    url = get_download_url(request.user, track_id)
    return JsonResponse({'download': url})


def get_thumbnail(request):
    track_id = request.GET.get('id')
    url = get_thumbnail_url(request.user, track_id)
    return JsonResponse({'thumbnail': url})
