from itertools import groupby
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
from providers.graph.content import get_track_download_url, get_track_thumbnail_url
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
    albums = queries.get_releases_query(request.user).order_by('name', 'year')
    data = {'albums': serializers.serialize_releases(albums)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_songs(request):
    songs = queries.get_tracks_query(request.user)
    data = {'songs': serializers.serialize_tracks(songs)}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_library(request):
    library = serializers.serialize_library(queries.get_releases_query(request.user))
    tracks = queries.get_tracks_query(request.user).order_by('release_id', 'position', 'name')
    grouped_tracks = {k: tuple(tracks) for k, tracks in groupby(tracks, lambda t: t.release_id)}

    for r in library:
        release_tracks = grouped_tracks[r['id']]
        r['tracks'] = serializers.serialize_tracks(release_tracks)
        r['track_count'] = len(release_tracks)

    data = {'library': library}
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_download(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_track_download_url(track)
    return JsonResponse({'download': url})


@login_required
def get_thumbnail(request):
    track_id = request.GET.get('id')
    track = get_object_or_404(Track, pk=track_id, user=request.user)
    url = get_track_thumbnail_url(track)
    return JsonResponse({'thumbnail': url})


@login_required
def get_album_details(request):
    album_id = request.GET.get('id')
    album = get_object_or_404(Release, pk=album_id, user=request.user)
    tracks = album.tracks.all()
    data = {
        'album': serializers.serialize_release(album),
        'tracks': serializers.serialize_tracks(tracks)
    }
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def get_artist_details(request):
    artist_id = request.GET.get('id')
    artist = get_object_or_404(Artist, pk=artist_id, user=request.user)

    releases = [{
        **serializers.serialize_release(release),
        'tracks': serializers.serialize_tracks(release.tracks.all())
    } for release in artist.releases.all()]

    data = {
        'artist': serializers.serialize_artist(artist),
        'releases': releases
    }
    return JsonResponse(data, encoder=ParlourJSONEncoder)


@login_required
def search(request):
    terms = request.GET.get('q', ''.strip())
    data = {'matches': []}

    if len(terms) < 2:
        return JsonResponse(data)

    artists = queries.get_search_artists_query(request.user, terms)[:5]
    releases = queries.get_search_releases_query(request.user, terms)[:5]
    tracks = queries.get_search_tracks_query(request.user, terms)[:5]

    data['matches'].extend([{**t, 'group': 0} for t in serializers.serialize_artists(artists)])
    data['matches'].extend([{**t, 'group': 1} for t in serializers.serialize_releases(releases)])
    data['matches'].extend([{**t, 'group': 2} for t in serializers.serialize_tracks(tracks)])

    return JsonResponse(data, encoder=ParlourJSONEncoder)


@require_POST
@login_required
def set_liked(request):
    data = get_body_json(request)
    track_id = data.get('id')
    liked = data.get('liked')
    success = commands.set_track_liked(request.user, track_id, liked)
    return JsonResponse({'success': success})
