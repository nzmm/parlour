from django.db import models
from django.contrib.auth.models import User
from server.common.caching import release_thumbnail_upload_to


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    provider = models.CharField(max_length=8)
    value = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.user.email} ({self.provider})"


class Artist(models.Model):
    class Meta:
        ordering = ('name',)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_artists")
    name = models.CharField(max_length=255)
    thumbnail = models.FileField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Release(models.Model):
    class Meta:
        ordering = ('artist__name', 'name')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_releases")
    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(null=True)
    thumbnail = models.FileField(max_length=255, null=True, upload_to=release_thumbnail_upload_to)
    provider = models.CharField(max_length=8)
    provider_id = models.CharField(max_length=255, default="")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="releases")

    def __str__(self):
        return f"{self.name} ({self.year})"


class Track(models.Model):
    class Meta:
        ordering = ('artist__name', 'release_name', 'disc', 'position')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tracks")
    disc = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    number = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    release_name = models.CharField(max_length=255)
    artist_credit = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, default="")
    year = models.PositiveSmallIntegerField(null=True)
    thumbnail = models.CharField(max_length=255, default="", help_text="This is a copy of the related release thumbnail.url")
    length = models.PositiveIntegerField()
    length_display = models.CharField(max_length=50)
    bitrate = models.PositiveSmallIntegerField(null=True)
    liked = models.BooleanField(default=False)
    provider = models.CharField(max_length=8)
    provider_id = models.CharField(max_length=255, default="")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="tracks")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_tracks")

    def __str__(self):
        return f"{self.name} ({self.provider_id})"
