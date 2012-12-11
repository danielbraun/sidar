from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from models import *
from imagekit.admin import AdminThumbnail

models = [Country, Discipline, Generation, Category, Subject]


class TranslatedModelAdmin(TranslationAdmin):
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class WorkAdmin(TranslationAdmin):
    # search_fields = ['designer__name_he', 'category__name_he', ]
    # list_display = ('__unicode__', 'designer', 'category', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='preview_image')
    filter_horizontal = ['subjects', ]
    list_display = ('name_he', 'designer', 'discipline')
    ordering = ('name_he',)


class DesignerAdmin(TranslationAdmin):
    # list_display = ('name_en', 'name_ar', 'main_discipline', 'work_count')
    list_display = ('name_he', 'main_discipline', 'work_count')
    # list_filter = ('main_discipline',)
    ordering = ('name_he',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Designer, DesignerAdmin)

for model in models:
    admin.site.register(model, TranslatedModelAdmin)
