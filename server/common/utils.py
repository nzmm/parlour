import json


def get_body_json(request):
    return json.loads(request.body)


def get_display_length(ms):
    s = int((ms / 1000) % 60)
    m = int((ms / (1000 * 60)) % 60)
    h = int((ms / (1000 * 60 * 60)) % 24)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def get_user_initials(user):
    first = user.first_name.strip()
    last = user.last_name.strip()

    if first and last:
        return f"{first[0]}{last[0]}".upper()

    return user.username[:2].upper()