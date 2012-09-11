from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from models import *

models = [Designer, Work, Country, Discipline, Category, Client, Technique, Collection, Subject, Generation]

class TranslatedModelAdmin(TranslationAdmin):
	# pass
	list_display = ('name', 'name_he','name_en')

for model in models:
	admin.site.register(model, TranslatedModelAdmin)