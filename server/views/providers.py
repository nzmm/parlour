from itertools import groupby
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from server.graph.auth import get_sign_in_url, get_token_from_code, get_token, store_token, remove_token
from server.common import queries
from server.common import commands
from server.common import serializers
from server.common.encoders import ParlourJSONEncoder
from server.graph.content import get_track_download_url, get_track_thumbnail_url
from server.common.utils import get_body_json
from server.models import Artist, Release, Track


@login_required
def graph_sign_in(request):
    sign_in_url, state = get_sign_in_url()
    request.session['auth_state'] = state
    return HttpResponseRedirect(sign_in_url)


@login_required
def graph_sign_out(request):
    remove_token(request.user)
    return HttpResponseRedirect(reverse('home'))


def graph_callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = get_token_from_code(request.get_full_path(), expected_state)
    store_token(request.user, token)
    return HttpResponseRedirect(reverse('home'))
