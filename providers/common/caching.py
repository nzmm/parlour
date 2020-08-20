import os
import hashlib
import requests
import shutil
from pathlib import Path
from parlour.settings import MEDIA_ROOT


def get_media_user_facet(user):
    return Path(hashlib.sha224(f"user.email:{user.id}".encode('utf-8')).hexdigest())


def get_cache_dir(user, role):
    user_facet = get_media_user_facet(user)
    return user_facet / role


def get_coverart_cache_path(release):
    d = get_cache_dir(release.user, "coverart")
    path = d / f"{release.id}.jpg"
    return path


def fetch_file(url):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    return r.raw


def release_thumbnail_upload_to(release, _):
    return get_coverart_cache_path(release)


def track_cache_thumbnail(track, url):
    f = fetch_file(url)

    release = track.release
    release.thumbnail.save('coverart.jpg', f)
    release.save()

    media_url = release.thumbnail.url
    release.tracks.update(thumbnail=media_url)

    return media_url
