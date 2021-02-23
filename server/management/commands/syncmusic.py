from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from server.graph.auth import PROVIDER_GRAPH
from server.graph.sync import sync_music as graph_sync_music


class Command(BaseCommand):
    help = 'Sync music for a given provider and user (specified by email)'

    def add_arguments(self, parser):
        parser.add_argument('--user', type=str)
        parser.add_argument('--provider', type=str)
        return

    def handle(self, *args, **options):
        user = options['user']
        provider = options['provider']

        user = User.objects.get(username=user)
        if not user:
            raise CommandError(f"No user with matching email:{user}")

        if provider == PROVIDER_GRAPH:
            graph_sync_music(user)

        self.stdout.write(self.style.SUCCESS('Successfully synced'))
        return
