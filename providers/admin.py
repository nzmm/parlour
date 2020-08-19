from django.contrib import admin
from providers.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "modified")
    list_filter = ('provider',)
