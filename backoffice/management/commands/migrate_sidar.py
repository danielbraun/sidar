# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from backoffice.models import Generation, Designer
from backoffice.sidar_models import Designerscategory, Designers
from backoffice.utils import emptify
from html2text import html2text
from sidar.settings import LEGACY_DB_NAMES







class Command(BaseCommand):
    help = "Converts old sidar models and tables to new ones"

    def handle(self, *args, **options):
        for db_name in LEGACY_DB_NAMES:

            # Generation migration
            for generation in Designerscategory.objects.using(db_name).all():
                Generation(
                    id=generation.catcode,
                    name_he=generation.name
                ).save()

            # Designer Migration
            for object in Designers.objects.using(db_name).all():
                Designer(
                    name_he=object.namehebrew,
                    name_en=object.nameenglish,
                    birth_country=(Country.objects.get_or_create(name_he=nullify(object.birthcountry)))[0],
                    is_active=object.status,
                    generation_id=object.catcode,
                    philosophy_summary_he=html2text(emptify(object.comments).strip())
                ).save()

            # Client migration from sidar_items
            # for object in SidarItems.objects.using("legacy").all():
                # Client.objects.get_or_create(name_he=nullify(object.client_he), defaults={'name_en': object.client})
