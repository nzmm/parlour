from json import loads

ATTR_SPLITTER = '__'

DEFAULT_ARTIST_FIELDS = (
    'id',
    'name')

DEFAULT_ALBUM_FIELDS = (
    'id',
    'name',
    'thumbnail')

DEFAULT_SONG_FIELDS = (
    'id',
    'number',
    'name',
    'artist_credit',
    'release_name',
    'year',
    'length_display',
    'thumbnail',
    'liked')

DEFAULT_ARTIST_DETAIL_FIELDS = (
    'id',
    'name')

DEFAULT_ALBUM_DETAIL_FIELDS = (
    'id',
    'name',
    'thumbnail',
    'year',
    'artist__name')


def getattr_nested(obj, field):
    attrs = field.split(ATTR_SPLITTER)
    for a in attrs[:-1]: obj = getattr(obj, a)
    return  getattr(obj, attrs[-1])


def get_nested_fields(obj, fields):
    return {f.replace(ATTR_SPLITTER, '_'): getattr_nested(obj, f) for f in fields}


def get_fields(obj, fields):
    return {f: getattr(obj, f) for f in fields}


def serialize_artists(queryset, fields=DEFAULT_ARTIST_FIELDS):
    return [get_fields(o, fields) for o in queryset]


def serialize_releases(queryset, fields=DEFAULT_ALBUM_FIELDS):
    return [get_fields(o, fields) for o in queryset]


def serialize_tracks(queryset, fields=DEFAULT_SONG_FIELDS):
    return [get_fields(o, fields) for o in queryset]


def serialize_artist(obj, fields=DEFAULT_ARTIST_DETAIL_FIELDS):
    return get_fields(obj, fields)


def serialize_release(obj, fields=DEFAULT_ALBUM_DETAIL_FIELDS):
    return get_nested_fields(obj, fields)
