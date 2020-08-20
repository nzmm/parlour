from providers.graph.auth import PROVIDER_GRAPH, get_token
from providers.graph.requests import get_music_children, get_children
from providers.models import Artist, Release, Track
from providers.common.utils import get_display_length


def get_track_name(f, audio):
    name = audio.get('title', '').strip()
    if not name:
        name = f.get('name', f"Untitled ({f['id']})").strip()
    return name


def store_audio(user, f, audio):
    artist, _ = Artist.objects.get_or_create(
        user=user,
        name=audio.get('albumArtist', ''))

    release, _ = Release.objects.update_or_create(
        user=user,
        name=audio.get('album'),
        year=audio.get('year'),
        artist=artist)

    driveitem_id = f.get('id')
    length = audio.get('duration', 0)

    track, created = Track.objects.update_or_create(
        user=user,
        provider=PROVIDER_GRAPH,
        provider_id=driveitem_id,
        defaults={
            'disc': audio.get('disc', 0),
            'position': audio.get('track', 0),
            'number': audio.get('track', ''),
            'name': get_track_name(f, audio),
            'release_name': audio.get('album'),
            'artist_credit': audio.get('artist', ''),
            'genre': audio.get('genre', ''),
            'year': audio.get('year'),
            'length': length,
            'length_display': get_display_length(length),
            'bitrate': audio.get('bitrate'),
            'artist': artist,
            'release': release,
        })

    print(f'[{user.email}] Track {"created" if created else "synced"}: {track}')
    return


def handle_file(user, f):
    audio = f.get('audio')
    if not audio:
        return

    store_audio(user, f, audio)
    return


def handle_folder(user, d):
    child_count = d['folder'].get('childCount')
    if not child_count:
        return []

    token = get_token(user)
    driveitem_id = d.get('id')
    children = get_children(token, driveitem_id).get('value', [])
    return children


def walk(user, parent, children):
    print(f"Walking {len(children)} children...")

    if not children:
        return

    for item in children:
        if item.get('file'):
            handle_file(user, item)
        elif item.get('folder'):
            children = handle_folder(user, item)
            walk(user, item, children)
    return


def sync_music(user):
    token = get_token(user)
    if not token:
        return False

    music = get_music_children(token)
    walk(user, {}, music.get('value', []))
    return True
