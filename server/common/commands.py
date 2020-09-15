from server.models import Track, ChannelTrack


def set_track_liked(user, track_id, liked):
    matches = Track.objects.filter(user=user, id=track_id).update(liked=liked)
    return matches > 0


def create_channel(user, name, desc, public):
    channel = user.channels.create(name=name, description=desc, public=public)
    return True, channel.unique_id


def create_channel_track(user, channel_id, track_id):
    channel = user.channels.get(unique_id=channel_id)
    track = user.user_tracks.get(id=track_id)

    ch_track = ChannelTrack.objects.create(
        user=user,
        channel=channel,
        track=track)

    ch_track.save()

    return True, ch_track.id
