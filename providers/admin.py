from django.contrib import admin
from providers.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "modified")
    list_filter = ('type',)
