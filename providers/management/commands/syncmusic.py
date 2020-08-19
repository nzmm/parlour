from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from providers.models import Token
from providers.graph.auth import PROVIDER_GRAPH, get_token as graph_get_token
from providers.graph.sync import sync_music as graph_sync_music


class Command(BaseCommand):
    help = 'Sync music for a given provider and user (specified by email)'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str)
        parser.add_argument('--provider', type=str)
        return

    def handle(self, *args, **options):
        email = options['email']
        provider = options['provider']

        user = User.objects.get(email=email)
        if not user:
            raise CommandError(f"No user with matching email:{email}")

        if provider == PROVIDER_GRAPH:
            graph_sync_music(user)

        self.stdout.write(self.style.SUCCESS('Successfully synced'))
        return
