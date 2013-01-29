from modeltranslation.translator import translator, TranslationOptions
from backoffice.models import *

models = [Country, Category, Client, Technique, Collection, Subject, Generation, Keyword]


class CommonModelTranslationOptions(TranslationOptions):
    fields = ('name',)


class DisciplineTranslationOptions(TranslationOptions):
    fields = ('name', 'info')


class DesignerTranslationOptions(CommonModelTranslationOptions):
    fields = ('name', 'philosophy_summary',)


class WorkTranslationOptions(CommonModelTranslationOptions):
    # fields = ('name', 'description', 'publish_date_as_text', 'size_as_text')
    fields = ('name', 'description')

translator.register(Designer, DesignerTranslationOptions)
translator.register(Work, WorkTranslationOptions)
translator.register(Discipline, DisciplineTranslationOptions)

for model in models:
    translator.register(model, CommonModelTranslationOptions)
