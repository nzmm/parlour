from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    type = models.CharField("", max_length=50)
    value = models.TextField("")
    created = models.DateTimeField("", auto_now=False, auto_now_add=True)
    modified = models.DateTimeField("", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.type
