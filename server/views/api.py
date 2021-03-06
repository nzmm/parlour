from itertools import groupby
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from server.common import queries
from server.common import commands
from server.common import serializers
from server.common.encoders import TWJSONEncoder
from server.graph.content import get_track_download_url, get_track_thumbnail_url
from server.common.utils import get_body_json, get_user_initials
from server.models import Artist, Release, Track, Channel


ALL_PROVIDERS = [
    ("dropbox", "Dropbox", "/static/data/im/dropbox.svg"),
    ("google-drive", "Google Drive", "/static/data/im/google-drive.svg"),
    ("graph", "Microsoft OneDrive", "/static/data/im/onedrive.svg"),
]


@login_required
def get_current_user(request):
    user = request.user
    active_providers = {provider:id for (provider, id) in user.tokens.all().values_list('provider', 'id')}
    providers = [dict(provider=p, title=t, brand=b, id=active_providers.get(p)) for p, t, b in ALL_PROVIDERS]

    data = {
        'username': user.username,
        'first_name': user.first_name,
        'full_name': user.get_full_name() or user.username,
        'initials': get_user_initials(user),
        'providers': providers
    }
    return JsonResponse({'user': data})


@login_required
def get_artists(request):
    artists = queries.get_artists_query(request.user)
    data = {'artists': serializers.serialize_artists(artists)}
    return JsonResponse(data, encoder=TWJSONEncoder)


@login_required
def get_albums(request):
    albums = queries.get_releases_query(request.user).order_by('name', 'year')
    data = {'albums': serializers.serialize_releases(albums)}
    return JsonResponse(data, encoder=TWJSONEncoder)


@login_required
def get_songs(request):
    songs = queries.get_tracks_query(request.user)
    data = {'songs': serializers.serialize_tracks(songs)}
    return JsonResponse(data, encoder=TWJSONEncoder)


@login_required
def get_library(request):
    artists = serializers.serialize_artists(queries.get_artists_query(request.user))
    releases = serializers.serialize_library(queries.get_releases_query(request.user))
    tracks = queries.get_tracks_query(request.user).order_by('release_id', 'position', 'name')
    grouped_tracks = {k: tuple(tracks) for k, tracks in groupby(tracks, lambda t: t.release_id)}

    for r in releases:
        release_tracks = grouped_tracks[r['id']]
        r['tracks'] = serializers.serialize_tracks(release_tracks)
        r['track_count'] = len(release_tracks)

    data = {
        'artists': artists,
        'releases': releases,
        'track_count': tracks.count()
    }
    return JsonResponse(data, encoder=TWJSONEncoder)


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
    return JsonResponse(data, encoder=TWJSONEncoder)


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
    return JsonResponse(data, encoder=TWJSONEncoder)


@login_required
def get_channels(request):
    channels = serializers.serialize_channels(queries.get_channels_query(request.user))
    return JsonResponse({'channels': channels})


@login_required
def get_channel_tracks(request):
    channel_id = request.GET.get('channel_id')
    channel = get_object_or_404(Channel, unique_id=channel_id, user=request.user)
    tracks = channel.channel_tracks.select_related('track').all()
    return JsonResponse({'tracks': serializers.serialize_channel_tracks(tracks)})


@login_required
def search(request):
    terms = request.GET.get('q', ''.strip())
    data = {'matches': []}

    if len(terms) < 2:
        return JsonResponse(data)

    artists = queries.get_search_artists_query(request.user, terms)[:10]
    releases = queries.get_search_releases_query(request.user, terms)[:10]
    tracks = queries.get_search_tracks_query(request.user, terms)[:10]

    data['matches'].extend([{**t, 'group': 0} for t in serializers.serialize_artists(artists)])
    data['matches'].extend([{**t, 'group': 1} for t in serializers.serialize_releases(releases)])
    data['matches'].extend([{**t, 'group': 2} for t in serializers.serialize_tracks(tracks)])

    return JsonResponse(data, encoder=TWJSONEncoder)


@require_POST
@login_required
def set_liked(request):
    data = get_body_json(request)
    track_id = data.get('id')
    liked = data.get('liked')
    success = commands.set_track_liked(request.user, track_id, liked)
    return JsonResponse({'success': success})


@require_POST
@login_required
def create_channel(request):
    data = get_body_json(request)
    name = data.get('name')
    description = data.get('description')
    public = data.get('public')
    success, channel_id = commands.create_channel(request.user, name, description, public)
    return JsonResponse({'success': success, 'channel_id': channel_id})


@require_POST
@login_required
def create_channel_track(request):
    data = get_body_json(request)
    channel_id = data.get('channel_id')
    track_id = data.get('track_id')
    success, ch_track_id = commands.create_channel_track(request.user, channel_id, track_id)
    return JsonResponse({'success': success, 'channel_track_id': ch_track_id})
