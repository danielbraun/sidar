# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from backoffice.models import Generation, Designer, Country, Work, Client
from backoffice.sidar_models import Designerscategory, Designers, SidarItems

from sidar.settings import LANGUAGES
from django.utils import translation
from utils import nullify, emptify

class Command(BaseCommand):
	help = "Converts old sidar models and tables to new ones"
	def handle(self, *args, **options):
		# Generation migration
		for object in Designerscategory.objects.using("legacy").all():
			Generation(id=object.catcode, name_he=object.name).save()

		# Designer Migration
		for object in Designers.objects.using("legacy").all():
			Designer(
				name_he=object.namehebrew, 
				name_en=object.nameenglish,
				# birth_country=(Country.objects.get_or_create(name_he=nullify(object.birthcountry)))[0],
				is_active=object.status,
				generation_id=object.catcode,
				philosophy_summary_he=emptify(object.comments)
			).save()

		# Client migration from sidar_items
		# for object in SidarItems.objects.using("legacy").all():
			# Client.objects.get_or_create(name_he=nullify(object.client_he), defaults={'name_en': object.client})


