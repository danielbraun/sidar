# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.processors.crop import TrimBorderColor
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django_countries import CountryField


class FilterableByDesignerMixin(object):

    def designers_by_discipline(self, discipline):
        designer_ids = self.work_set.filter(discipline=discipline).values_list('designer', flat=True).distinct()
        return Designer.objects.filter(pk__in=designer_ids)


class CommonModel(models.Model):
    name = models.CharField(u'שם', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name_he']


class GenericManager(models.Manager):
    def belonging_to_discipline(self, discipline, field):
        return self.filter(pk__in=Work.objects.filter(discipline=discipline).values(field).distinct())


class Discipline(CommonModel):
    # info = models.TextField(u'מידע על הדיסיפלינה')
    info = HTMLField()
    active = models.BooleanField(u'פעיל')

    def work_count(self):
        return self.work_set.count()
    work_count.short_description = u'מספר עבודות'

    def short_name(self):
        return u'ע.' + self.name

    def long_name(self):
        return u'עיצוב ' + self.name

    def get_absolute_url(self):
        return reverse('discipline-about', kwargs={'discipline': self.id})

    class Meta(CommonModel.Meta):
        verbose_name = u'תחום עיצוב'
        verbose_name_plural = u'תחומי עיצוב'


class DesignerManager(GenericManager):
    def specializing_in(self, discipline):
        result = []
        for designer in Designer.objects.all():
            if designer.main_discipline() == discipline:
                result.append(designer)
        return result


class MainDisciplineMethodMixin(object):
    def main_discipline(self):
        try:
            key = self.work_set.values('discipline').annotate(dcount=Count('discipline')).order_by('-dcount')[0]['discipline']
        except IndexError:
            return None
        return Discipline.objects.get(id=key)
    main_discipline.short_description = u'תחום עיצוב עיקרי'


class Designer(CommonModel, MainDisciplineMethodMixin):
    def get_absolute_url(self):
        return reverse('designer-detail', kwargs={
            'discipline': self.main_discipline().id,
            'pk': self.id,
        })

    def work_count(self):
        return self.work_set.count()
    work_count.short_description = u'מספר עבודות'

    def available_categories_by_discipline(self, discipline):
        category_ids = self.work_set.filter(discipline=discipline).values_list('category', flat=True).distinct()
        return Category.objects.filter(pk__in=category_ids)

    def photo_as_img(self):
        url = "asdasd"
        if self.photo:
            url = self.photo.url
        return u'<img src="%s" class="thumbnail"/>' % (url)
    photo_as_img.allow_tags = True
    photo_as_img.short_description = u'תמונת מעצב'

    objects = DesignerManager()

    generation = models.ForeignKey("Generation", verbose_name="שייך לדור", null=True)
    photo = models.ImageField(u'תמונת מעצב', upload_to="images/", blank=True)
    birth_year = models.IntegerField(u'שנת לידה', blank=True, null=True)
    death_year = models.IntegerField(u'שנת פטירה', blank=True, null=True)
    birth_country = CountryField(u'מדינת לידה', null=True, blank=True, default='IL')
    philosophy_summary = HTMLField(u'תקציר פילוסופיה', blank=True)
    philosophy = models.FileField(u'קובץ פילוסופיה', upload_to="pdf/", blank=True)
    is_active = models.BooleanField(u'פעיל/ה', default=False)

    class Meta(CommonModel.Meta):
        verbose_name = "מעצב"
        verbose_name_plural = "מעצבים"


class Collector(CommonModel):
    photo = models.ImageField(u'תמונת אספן', upload_to="images/", blank=True)
    birth_year = models.IntegerField(u'שנת לידה', blank=True, null=True)
    death_year = models.IntegerField(u'שנת פטירה', blank=True, null=True)
    homepage = models.URLField(u'אתר בית', blank=True)
    birth_country = CountryField(u'מדינת לידה', null=True, blank=True, default='IL')
    philosophy_summary = HTMLField(u'תקציר פילוסופיה', blank=True)
    philosophy = models.FileField(u'קובץ פילוסופיה', upload_to="pdf/", blank=True)
    is_active = models.BooleanField(u'פעיל/ה', default=False)

    class Meta(CommonModel.Meta):
        verbose_name = u'אספן'
        verbose_name_plural = u'אספנים'


class WorkManager(models.Manager):
    def one_from_each_discipline(self):
        works = []
        i = 0
        while i < 10:
            i = i + 1
            for discipline in Discipline.objects.filter(active=True):
                try:
                    works.append(discipline.work_set.filter(designer__isnull=False).order_by('?')[0])
                except IndexError:
                    pass
        return works


class Work(CommonModel):
    DATE_ACCURACY_LEVELS = (
        ('de', u'עשור'),
        ('y', u'שנה'),
        ('m', u'חודש'),
        ('d', u'יום')
    )

    objects = WorkManager()
    tags = TaggableManager(u'מילות מפתח')

    sidar_id = models.CharField(u'קוד עבודה', max_length=50, blank=True)
    designer = models.ForeignKey('Designer', verbose_name=u'מעצב', null=True)
    raw_image = models.ImageField(u'תמונת מקור', upload_to='works', null=True)
    processed_image = ImageSpecField(
        processors=[ResizeToFit(width=400),
                    TrimBorderColor(sides=('t', 'r', 'b', 'l'))],
        image_field='raw_image')
    discipline = models.ForeignKey("Discipline", verbose_name=u'תחום', null=True)
    category = models.ForeignKey("Category", verbose_name=u'קטגוריה', null=True)
    of_collections = models.ManyToManyField('Collector', verbose_name=u'מאוספים',
                                            related_name='work_collections')
    is_self_collected = models.BooleanField(u'מאוסף המעצב?')
    subjects = models.ManyToManyField("Subject", verbose_name=u'נושאים', blank=True)
    # Date related fields
    publish_date_as_text = models.CharField(u'תאריך כמלל', max_length=50, blank=True)
    # publish_date = models.DateField(verbose_name="תאריך הוצאה לאור", null=True)
    # date_accuracy_level = models.CharField(u'רמת דיוק תאריך', max_length=2,
    # choices=DATE_ACCURACY_LEVELS, default=None, blank=True)
    publish_year = models.IntegerField('שנה', null=True, blank=True, help_text=u'שנה לועזית')
    # Size related fields
    size_as_text = models.CharField(u'גודל כמלל', max_length=128, blank=True)
    height = models.DecimalField(u'גובה', max_digits=5, decimal_places=2, default=0, blank=True)
    width = models.DecimalField(u'רוחב', max_digits=5, decimal_places=2, default=0, blank=True)
    depth = models.DecimalField(u'עומק', max_digits=5, decimal_places=2, default=0, blank=True)

    client = models.CharField(u'לקוח', max_length=255, blank=True)
    country = CountryField(u'מדינה', null=True, blank=True, default='IL')
    technique = models.CharField(u'טכניקה', max_length=255, blank=True)

    description = models.TextField(u'תיאור', blank=True)

    class Meta(CommonModel.Meta):
        verbose_name = "עבודה"
        verbose_name_plural = "עבודות"

    def __unicode__(self):
        return self.sidar_id

    def get_absolute_url(self):
        return reverse('work-detail', kwargs={
            'discipline': self.discipline.id,
            'designer': self.designer.id,
            'work': self.id
        })


class Category(CommonModel, FilterableByDesignerMixin, MainDisciplineMethodMixin):
    parent = models.ForeignKey('self', verbose_name=u'קטגורית על', blank=True, null=True)
    info = models.TextField(u'מידע על הקטגוריה')
    objects = GenericManager()

    class Meta(CommonModel.Meta):
        verbose_name = "קטגוריה"
        verbose_name_plural = "קטגוריות"

    def get_absolute_url(self):
        return reverse('work-list', kwargs={
            'discipline': self.main_discipline().id,
            'category': self.id,
        })


class Subject(CommonModel, FilterableByDesignerMixin, MainDisciplineMethodMixin):
    parent = models.ForeignKey('self', verbose_name=u'נושא על', blank=True, null=True)
    info = models.TextField(u'מידע על הנושא')
    objects = GenericManager()

    class Meta(CommonModel.Meta):
        verbose_name = "נושא"
        verbose_name_plural = "נושאים"

    def get_absolute_url(self):
        return reverse('work-list', kwargs={
            'discipline': self.main_discipline().id,
            'subject': self.id,
        })


class Generation(CommonModel):

    class Meta(CommonModel.Meta):
        verbose_name = u'דור מעצבים'
        verbose_name_plural = u'דורות מעצבים'


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # Custom fields
    in_charge_of_designers = models.ManyToManyField(Designer, verbose_name=u'אחראי על מעצבים', blank=True)
    # portrait = models.ImageField(upload_to='portraits/', null=True)

    class Meta:
        verbose_name = u'פרופיל משתמש'
        verbose_name_plural = u'פרופילי משתמש'


def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
