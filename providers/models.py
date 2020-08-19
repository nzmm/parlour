from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    provider = models.CharField(max_length=8)
    value = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.type


class Artist(models.Model):
    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=255)


class Release(models.Model):
    class Meta:
        ordering = ('year',)

    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="releases")


class Track(models.Model):
    class Meta:
        ordering = ('disc', 'position')

    disc = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    number = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    artist_credit = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, default="")
    year = models.PositiveSmallIntegerField(null=True)
    length = models.PositiveIntegerField()
    bitrate = models.PositiveSmallIntegerField(null=True)
    provider = models.CharField(max_length=8)
    download_url = models.TextField()
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="tracks")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_tracks")
