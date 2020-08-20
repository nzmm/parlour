from django.contrib import admin
from providers.models import (
    Token,
    Artist,
    Release,
    Track)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "modified")
    list_filter = ('provider',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("user", "name")


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ("user", "name")


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "name")
    list_filter = ('provider',)
    read_only = ('provider', 'provider_id')
