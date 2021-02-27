from django.urls import path
from server.views import providers

urlpatterns = [
    path('<int:provider_id>/refresh_music/', providers.refresh_music, name='refresh_music'),
    path('<int:provider_id>/refresh_thumbs/', providers.refresh_thumbs, name='refresh_thumbs'),
    path('graph_signin', providers.graph_sign_in, name='graph_signin'),
    path('graph_signout', providers.graph_sign_out, name='graph_signout'),
    path('graph_callback', providers.graph_callback, name='graph_callback'),
]