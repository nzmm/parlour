"""parlour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from providers import views

urlpatterns = [
    path('graph_signin', views.graph_sign_in, name='graph_signin'),
    path('graph_signout', views.graph_sign_out, name='graph_signout'),
    path('graph_callback', views.graph_callback, name='graph_callback'),

    path('get_artists', views.get_artists, name='get_artists'),
    path('get_albums', views.get_albums, name='get_albums'),
    path('get_songs', views.get_songs, name='get_songs'),
    path('get_download', views.get_download, name='get_download'),
    path('get_thumbnail', views.get_thumbnail, name='get_thumbnail'),
    path('get_artist_details', views.get_artist_details, name='get_artist_details'),
    path('get_album_details', views.get_album_details, name='get_album_details'),

    path('set_liked', views.set_liked, name='set_liked')
]