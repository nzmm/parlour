from providers.models import Artist, Release, Track


def get_artists_query(user):
    return Artist.objects.filter(user=user)


def get_albums_query(user):
    return Release.objects.filter(user=user)


def get_songs_query(user):
    return Track.objects.filter(user=user)
