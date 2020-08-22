from providers.models import Track


def set_track_liked(user, track_id, liked):
    matches = Track.objects.filter(user=user, id=track_id).update(liked=liked)
    return matches > 0
