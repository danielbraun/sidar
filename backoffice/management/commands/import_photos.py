from django.core.management.base import BaseCommand
from django.conf import settings
from backoffice.models import Work
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        for root, dirs, files in os.walk(settings.PORFOLIO_IMAGE_DIR):
            for name in files:
                full_path = os.path.join(root, name)
                print full_path
                Work.create_from_photo(full_path)
                os.remove(full_path)
                i = i + 1
        print "%s images." % i
