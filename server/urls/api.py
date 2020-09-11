from django.urls import path
from server.views import api

urlpatterns = [
    path('get_current_user', api.get_current_user, name='get_current_user'),
    path('get_artists', api.get_artists, name='get_artists'),
    path('get_albums', api.get_albums, name='get_albums'),
    path('get_songs', api.get_songs, name='get_songs'),
    path('get_library', api.get_library, name='get_library'),
    path('get_download', api.get_download, name='get_download'),
    path('get_thumbnail', api.get_thumbnail, name='get_thumbnail'),
    path('get_artist_details', api.get_artist_details, name='get_artist_details'),
    path('get_album_details', api.get_album_details, name='get_album_details'),
    path('search', api.search, name='search'),

    path('create_channel', api.create_channel, name='create_channel'),
    path('set_liked', api.set_liked, name='set_liked'),
]