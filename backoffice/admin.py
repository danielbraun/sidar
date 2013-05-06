# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from imagekit.admin import AdminThumbnail
from modeltranslation.admin import TranslationAdmin

import models
from django.contrib.auth.admin import UserAdmin


regular_models = [models.Generation, models.Category, models.Subject, models.Collector]
TranslationAdmin.actions_on_bottom = True
TranslationAdmin.actions_on_top = False
TranslationAdmin.ordering = ('name_he',)


class TranslatedModelAdmin(TranslationAdmin):
    # search_fields = ['name_he']
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class DisciplineAdmin(TranslationAdmin):
    list_display = ('name_he', 'name_en', 'active', 'work_count')


class WorkAdmin(TranslationAdmin):
    # search_fields = ['designer__name_he', 'category__name_he', ]
    # list_display = ('__unicode__', 'designer', 'category', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='processed_image')
    admin_thumbnail.short_description = u'תצוגה מקדימה'

    # filter_horizontal = ['subjects', 'keywords']
    list_display = ('sidar_id', 'name', 'designer', 'category', 'discipline', 'admin_thumbnail')
    # list_editable = ('designer',)
    # list_display = ('size_as_text', 'client', 'publish_date_as_text',)
    ordering = ('-id',)
    list_filter = ('discipline', 'category', 'designer',)

    def queryset(self, request):
        qs = super(WorkAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(designer=request.user.get_profile().in_charge_of_designers.all())


class DesignerAdmin(TranslationAdmin):
    list_display = ('name', 'main_discipline', 'generation', 'birth_year', 'work_count', 'is_active')
    list_filter = ('generation', 'is_active')


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile


class UserAdmin(UserAdmin):
    search_fields = ()
    list_filter = ()
    inlines = (UserProfileInline, )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'get_designers')

    def get_designers(self, instance):
        names = [item.name for item in instance.get_profile().in_charge_of_designers.all()]
        return ', '.join(names)
    get_designers.short_description = u'מעצבים בטיפול'


admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.Designer, DesignerAdmin)
admin.site.register(models.Discipline, DisciplineAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

for model in regular_models:
    admin.site.register(model, TranslatedModelAdmin)
