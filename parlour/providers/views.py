from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from providers.graph.auth_helper import get_sign_in_url, get_token_from_code, store_token
from providers.graph.graph_helper import get_user


def graph_sign_in(request):
    sign_in_url, state = get_sign_in_url()
    request.session['auth_state'] = state
    return HttpResponseRedirect(sign_in_url)


def graph_callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = get_token_from_code(request.get_full_path(), expected_state)

    user = get_user(token)
    print(user)

    store_token(request.user, token)
    return HttpResponseRedirect(reverse('home'))


def graph_sign_out(request):
    remove_token(request.user)
    return HttpResponseRedirect(reverse('home'))
