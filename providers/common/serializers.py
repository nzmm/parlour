from json import loads

DEFAULT_ARTIST_FIELDS = (
    'id',
    'name')

DEFAULT_ALBUM_FIELDS = (
    'id',
    'name')

DEFAULT_SONG_FIELDS = (
    'id',
    'number',
    'name',
    'artist_credit',
    'release_name',
    'year',
    'length_display',
    'thumbnail')


def get_fields(obj, fields):
    return {f: getattr(obj, f) for f in fields}


def serialize_artists(queryset, fields=DEFAULT_ARTIST_FIELDS):
    return [get_fields(o, fields) for o in queryset]


def serialize_albums(queryset, fields=DEFAULT_ALBUM_FIELDS):
    return [get_fields(o, fields) for o in queryset]


def serialize_songs(queryset, fields=DEFAULT_SONG_FIELDS):
    return [get_fields(o, fields) for o in queryset]
