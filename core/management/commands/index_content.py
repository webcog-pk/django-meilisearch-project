from django.core.management import BaseCommand
from core.meilisearch import index_person_content

class Command(BaseCommand):
    help = "Start Index"

    def handle(self, *args, **kwargs):
        index_person_content()
        self.stdout.write(self.style.SUCCESS('Indexing Complete'))