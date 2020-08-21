from providers.models import Track


def set_track_liked(user, track_id, liked):
    return Track.objects.filter(user=user, id=track_id).update(liked=liked)
