# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from imagekit.admin import AdminThumbnail
from modeltranslation.admin import TranslationAdmin

import models
from django.contrib.auth.admin import UserAdmin


regular_models = [models.Generation, models.Category, models.Subject]


class TranslatedModelAdmin(TranslationAdmin):
    search_fields = ['name_he']
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class DisciplineAdmin(TranslationAdmin):
    list_display = ('name_he', 'name_en', 'active', 'work_count')


class WorkAdmin(TranslationAdmin):
    # search_fields = ['designer__name_he', 'category__name_he', ]
    # list_display = ('__unicode__', 'designer', 'category', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='processed_image')
    admin_thumbnail.short_description = u'תצוגה מקדימה'

    filter_horizontal = ['subjects', 'keywords']
    list_display = ('id', 'name', 'designer', 'discipline', 'admin_thumbnail')
    # list_editable = ('designer',)
    # list_display = ('size_as_text', 'client', 'publish_date_as_text',)
    ordering = ('name_he',)
    # list_filter = ('discipline', 'category', 'designer',)

    def queryset(self, request):
        qs = super(WorkAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(designer=request.user.get_profile().in_charge_of_designers.all())


class DesignerAdmin(TranslationAdmin):
    # list_display = ('name_en', 'name_ar', 'main_discipline', 'work_count')
    list_display = ('name_he', 'main_discipline', 'work_count', 'is_active')
    # list_filter = ('main_discipline',)
    ordering = ('name_he',)


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        self.list_display += ('get_designers',)

    def get_designers(self, instance):
        return instance.get_profile().in_charge_of_designers.all()


admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.Designer, DesignerAdmin)
admin.site.register(models.Discipline, DisciplineAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

for model in regular_models:
    admin.site.register(model, TranslatedModelAdmin)
