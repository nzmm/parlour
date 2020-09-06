from django.db.models import F, Count
from server.models import Artist, Release, Track


def get_artists_query(user):
    return Artist.objects.filter(user=user).annotate(track_count=Count('artist_tracks'))


def get_releases_query(user):
    return Release.objects.filter(user=user).annotate(artist_name=F('artist__name'))


def get_tracks_query(user):
    return Track.objects.filter(user=user)


def get_search_artists_query(user, term):
    return Artist.objects.filter(user=user, name__icontains=term).annotate(track_count=Count('artist_tracks'))


def get_search_releases_query(user, term):
    return get_releases_query(user).filter(name__icontains=term)


def get_search_tracks_query(user, term):
    return Track.objects.filter(user=user, name__icontains=term)
