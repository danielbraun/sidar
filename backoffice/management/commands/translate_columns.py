# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import DatabaseError


class Command(BaseCommand):
	help = "Convert hebrew columns to english ones"
	def handle(self, *args, **options):		
		cursor = connections['legacy'].cursor()
		fields = [
			('ארץ', 'country_he'),
			('גודל','size_he'),
			('טכניקה', 'technique_he'),
			('לקוח', 'client_he'),
			('מאוסף', 'collection_he'),
			('מעצב', 'designer_he'),
			('נושא', 'subject_he'),
			('קטגוריה', 'category_he'),
			('`שם העבודה`', 'title_he'),
			('תאור', 'description_he'),
			('תאריך', 'date_he')
		]

		for field in fields:
			if field[0] != 'תאור':
				field += ("varchar(255)",)
			else:
				field += ("LONGTEXT",)
			try:
				cursor.execute("alter table sidar_items change %s %s %s;" % field)
			except DatabaseError:
				pass
