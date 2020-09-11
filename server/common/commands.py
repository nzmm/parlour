from server.models import Track


def set_track_liked(user, track_id, liked):
    matches = Track.objects.filter(user=user, id=track_id).update(liked=liked)
    return matches > 0


def create_channel(user, name, desc, public):
    channel = user.channels.create(name=name, description=desc, public=public)
    return True, channel.unique_id
