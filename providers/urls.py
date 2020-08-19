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
    path('graph_get_albums', views.graph_get_albums, name='graph_get_albums'),
]