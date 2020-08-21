from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from providers.graph.auth import get_sign_in_url, get_token_from_code, get_token, store_token
from providers.common import queries
from providers.common import commands
from providers.common import serializers
from providers.common.encoders import ParlourJSONEncoder
from providers.graph.content import get_download_url, get_thumbnail_url
from providers.common.utils import get_body_json
from providers.models import Track


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
    data = {'artists': serializers.serialize_artists(artists)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


def get_albums(request):
    albums = queries.get_albums_query(request.user)
    data = {'albums': serializers.serialize_albums(albums)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


def get_songs(request):
    songs = queries.get_songs_query(request.user)
    data = {'songs': serializers.serialize_songs(songs)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


def get_download(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_download_url(track)
    return JsonResponse({'download': url})


def get_thumbnail(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_thumbnail_url(track)
    return JsonResponse({'thumbnail': url})


def set_liked(request):
    data = get_body_json(request)
    matches = commands.set_track_liked(request.user, data.get('id'), data.get('liked'))
    return JsonResponse({'success': matches > 0})
