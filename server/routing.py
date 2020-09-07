from django.urls import re_path
from server.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<channel_name>\w+)/$', ChatConsumer),
]