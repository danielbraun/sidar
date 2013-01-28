from django.contrib import admin
from imagekit.admin import AdminThumbnail
from modeltranslation.admin import TranslationAdmin

from models import *


models = [Discipline, Generation, Category, Subject]


class TranslatedModelAdmin(TranslationAdmin):
    search_fields = ['name']
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class WorkAdmin(TranslationAdmin):
    # search_fields = ['designer__name_he', 'category__name_he', ]
    # list_display = ('__unicode__', 'designer', 'category', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='preview_image')
    filter_horizontal = ['subjects', 'keywords']
    list_display = ('sidar_id', 'designer', 'discipline')
    # list_display = ('size_as_text', 'client', 'publish_date_as_text',)
    ordering = ('name_he',)
    list_filter = ('discipline', 'category', 'designer',)


class DesignerAdmin(TranslationAdmin):
    # list_display = ('name_en', 'name_ar', 'main_discipline', 'work_count')
    list_display = ('name_he', 'main_discipline', 'work_count', 'is_active')
    # list_filter = ('main_discipline',)
    ordering = ('name_he',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Designer, DesignerAdmin)

for model in models:
    admin.site.register(model, TranslatedModelAdmin)
