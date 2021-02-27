from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from server.graph.auth import get_sign_in_url, get_token_from_code, store_token, remove_token
from server.tasks import sync_music_task, sync_thumbs_task


@login_required
def refresh_music(request, provider_id):
    task = sync_music_task.delay(request.user.pk, provider_id)
    print(task)
    return JsonResponse({"success": True})


@login_required
def refresh_thumbs(request, provider_id):
    task = sync_thumbs_task.delay(request.user.pk, provider_id)
    print(task)
    return JsonResponse({"success": True})


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
