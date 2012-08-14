from modeltranslation.translator import translator, TranslationOptions
from models import *

models = [Country, Discipline, Category, Client, Technique, Collection, Subject, Generation]

class CommonModelTranslationOptions(TranslationOptions):
	fields = ('name',)

class DesignerTranslationOptions(CommonModelTranslationOptions):
	fields = ('name', 'philosophy_summary',)

class WorkTranslationOptions(CommonModelTranslationOptions):
	fields = ('name', 'description',)

translator.register(Designer, DesignerTranslationOptions)
translator.register(Work, WorkTranslationOptions)

for model in models:
	translator.register(model, CommonModelTranslationOptions)
