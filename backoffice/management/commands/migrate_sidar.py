from django.core.management.base import BaseCommand, CommandError


from backoffice.models import Generation, Designer, Country
from backoffice.sidar_models import Designerscategory, Designers

from sidar.settings import LANGUAGES
from django.utils import translation

def nullify(str):
	if str == "":
		str = None
	return str

def emptify(str):
	if str == None:
		str = ""
	return str

class Command(BaseCommand):
	help = "Converts old sidar models and tables to new ones"
	def handle(self, *args, **options):

		objects = Designerscategory.objects.using("legacy").all()
		for object in objects:
			Generation(id=object.catcode, name_he=object.name).save()

		objects = Designers.objects.using("legacy").all()
		for object in objects:
			Designer(
				name_he=object.namehebrew, 
				name_en=object.nameenglish,
				birth_country=(Country.objects.get_or_create(name_he=nullify(object.birthcountry)))[0],
				is_active=object.status,
				generation_id=object.catcode,
				philosophy_summary_he=emptify(object.comments)
			).save()