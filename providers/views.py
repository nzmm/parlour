from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from providers.graph.auth_helper import get_sign_in_url, get_token_from_code, get_token, store_token
from providers.graph.graph_helper import get_albums


def graph_sign_in(request):
    sign_in_url, state = get_sign_in_url()
    request.session['auth_state'] = state
    return HttpResponseRedirect(sign_in_url)


def graph_callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = get_token_from_code(request.get_full_path(), expected_state)
    store_token(request.user, token)
    return HttpResponseRedirect(reverse('home'))


def graph_sign_out(request):
    remove_token(request.user)
    return HttpResponseRedirect(reverse('home'))


def graph_get_albums(request):
    token = get_token(request.user)
    songs = get_albums(token)
    return JsonResponse(songs)
