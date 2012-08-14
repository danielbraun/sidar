from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from models import *

models = [Designer, Work, Country, Discipline, Category, Client, Technique, Collection, Subject, Generation]

for model in models:
	admin.site.register(model, TranslationAdmin)