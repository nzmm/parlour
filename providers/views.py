from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from providers.graph.auth import get_sign_in_url, get_token_from_code, get_token, store_token, remove_token
from providers.common import queries
from providers.common import commands
from providers.common import serializers
from providers.common.encoders import ParlourJSONEncoder
from providers.graph.content import get_download_url, get_thumbnail_url
from providers.common.utils import get_body_json
from providers.models import Artist, Release, Track


@login_required
def graph_sign_in(request):
    sign_in_url, state = get_sign_in_url()
    request.session['auth_state'] = state
    return HttpResponseRedirect(sign_in_url)


@login_required
def graph_sign_out(request):
    remove_token(request.user)
    return HttpResponseRedirect(reverse('home'))


def graph_callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = get_token_from_code(request.get_full_path(), expected_state)
    store_token(request.user, token)
    return HttpResponseRedirect(reverse('home'))


@login_required
def get_artists(request):
    artists = queries.get_artists_query(request.user)
    data = {'artists': serializers.serialize_artists(artists)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_albums(request):
    albums = queries.get_albums_query(request.user)
    data = {'albums': serializers.serialize_albums(albums)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_songs(request):
    songs = queries.get_songs_query(request.user)
    data = {'songs': serializers.serialize_songs(songs)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_download(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_download_url(track)
    return JsonResponse({'download': url})


@login_required
def get_thumbnail(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_thumbnail_url(track)
    return JsonResponse({'thumbnail': url})


@login_required
def get_album_details(request):
    album_id = request.GET.get('id')
    album = get_object_or_404(Release, pk=album_id, user=request.user)
    tracks = album.tracks.all()
    data = {
        'album': serializers.serialize_album(album),
        'tracks': serializers.serialize_songs(tracks)
    }
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_artist_details(request):
    artist_id = request.GET.get('id')
    artist = get_object_or_404(Artist, pk=artist_id, user=request.user)

    releases = [{
        **serializers.serialize_album(release),
        'tracks': serializers.serialize_songs(release.tracks.all())
    } for release in artist.releases.all()]

    data = {
        'artist': serializers.serialize_artist(artist),
        'releases': releases
    }
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@require_POST
@login_required
def set_liked(request):
    data = get_body_json(request)
    track_id = data.get('id')
    liked = data.get('liked')
    success = commands.set_track_liked(request.user, track_id, liked)
    return JsonResponse({'success': success})
