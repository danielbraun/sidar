from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline
from models import *
from imagekit.admin import AdminThumbnail

models = [Country, Discipline, Category, Client, Technique, Collection, Subject, Generation]

class TranslatedModelAdmin(TranslationAdmin):
	list_display = ('name', 'name_en')

class WorkAdmin(TranslationAdmin):
	search_fields   = ['designer__name_he', 'category__name_he',]
	list_display    = ('__unicode__', 'designer', 'category', 'admin_thumbnail',)
	admin_thumbnail = AdminThumbnail(image_field='preview_image')

class DesignerAdmin(TranslationAdmin):
	list_display = ('name', 'name_en', 'main_discipline', 'work_count')
	# list_filter = ('main_discipline',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Designer, DesignerAdmin)

for model in models:
	admin.site.register(model, TranslatedModelAdmin)