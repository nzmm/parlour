import os
import ast
import time
from requests_oauthlib import OAuth2Session
from server.models import Token

PROVIDER_GRAPH = "graph"

GRAPH_REQUIRED_SCOPES = "files.read offline_access"
GRAPH_AUTHORITY = "https://login.microsoftonline.com/common"
GRAPH_AUTH_ENDPOINT = "/oauth2/v2.0/authorize"
GRAPH_TOKEN_ENDPOINT = "/oauth2/v2.0/token"

authorize_url = f'{GRAPH_AUTHORITY}{GRAPH_AUTH_ENDPOINT}'
token_url = f'{GRAPH_AUTHORITY}{GRAPH_TOKEN_ENDPOINT}'
app_id = os.environ["GRAPH_APP_ID"]
app_secret = os.environ["GRAPH_APP_SECRET"]
redirect = os.environ["GRAPH_REDIRECT_URI"]


def get_sign_in_url():
    aad_auth = OAuth2Session(
        app_id,
        scope=GRAPH_REQUIRED_SCOPES,
        redirect_uri=redirect)

    sign_in_url, state = aad_auth.authorization_url(
        authorize_url, prompt='login')

    return sign_in_url, state


def get_token_from_code(callback_url, expected_state):
    aad_auth = OAuth2Session(
        app_id,
        state=expected_state,
        scope=GRAPH_REQUIRED_SCOPES,
        redirect_uri=redirect)

    token = aad_auth.fetch_token(
        token_url,
        client_secret=app_secret,
        authorization_response=callback_url)

    return token


def store_token(user, token):
    token_obj, created = Token.objects.update_or_create(
        user=user,
        provider=PROVIDER_GRAPH,
        defaults={
            'value': token
        })
    return token_obj, created


def get_token(user):
    token_obj = user.tokens.filter(provider=PROVIDER_GRAPH).first()

    token = token_obj.value if token_obj else None
    token = ast.literal_eval(token)

    if token:
        # check expiration
        now = time.time()
        expire_time = token['expires_at'] - 300

        if now >= expire_time:
            # refresh the token
            aad_auth = OAuth2Session(
                app_id,
                token=token,
                scope=GRAPH_REQUIRED_SCOPES,
                redirect_uri=redirect)

            refresh_params = {
                'client_id': app_id,
                'client_secret': app_secret,
            }

            print("Refreshing graph user token...")
            new_token = aad_auth.refresh_token(token_url, **refresh_params)

            store_token(user, new_token)

            return new_token
        else:
            return token


def remove_token(user):
    return user.tokens.filter(provider=PROVIDER_GRAPH).delete()
