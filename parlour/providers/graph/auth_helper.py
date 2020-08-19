import os
import ast
import time
import yaml
from requests_oauthlib import OAuth2Session
from providers.models import Token

# This is necessary for testing with non-HTTPS localhost
# Remove this if deploying to production
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# This is necessary because Azure does not guarantee
# to return scopes in the same case and order as requested
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

# Load the oauth_settings.yml file
stream = open('graph_oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
authorize_url = f'{settings["authority"]}{settings["authorize_endpoint"]}'
token_url = f'{settings["authority"]}{settings["token_endpoint"]}'


def get_sign_in_url():
    # Initialize the OAuth client
    aad_auth = OAuth2Session(settings['app_id'],
        scope=settings['scopes'],
        redirect_uri=settings['redirect'])

    sign_in_url, state = aad_auth.authorization_url(authorize_url, prompt='login')

    return sign_in_url, state


def get_token_from_code(callback_url, expected_state):
    # Initialize the OAuth client
    aad_auth = OAuth2Session(settings['app_id'],
        state=expected_state,
        scope=settings['scopes'],
        redirect_uri=settings['redirect'])

    token = aad_auth.fetch_token(token_url,
        client_secret = settings['app_secret'],
        authorization_response=callback_url)

    return token


def store_token(user, token):
    token_obj, created = Token.objects.update_or_create(user=user, type="graph", defaults={
      'value': token
    })
    return token_obj, created


def get_token(user):
    token_obj = user.tokens.filter(type="graph").first()

    token = token_obj.value if token_obj else None
    token = ast.literal_eval(token)

    if token != None:
        # check expiration
        now = time.time()
        expire_time = token['expires_at'] - 300

        if now >= expire_time:
            # refresh the token
            aad_auth = OAuth2Session(settings['app_id'],
                token = token,
                scope=settings['scopes'],
                redirect_uri=settings['redirect'])

            refresh_params = {
                'client_id': settings['app_id'],
                'client_secret': settings['app_secret'],
            }

            print("Refreshing graph user token...")
            new_token = aad_auth.refresh_token(token_url, **refresh_params)

            store_token(user, new_token)

            return new_token
        else:
            return token


def remove_token(user):
    return user.tokens.filter(type="graph").delete()
