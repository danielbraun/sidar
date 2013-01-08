# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.processors.crop import TrimBorderColor
# from django.utils.translation import ugettext_lazy as _
from django.db.models import Count


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

    def with_parents_as_tree(self, discipline, field):
        tree = []
        discipline_subjects = self.belonging_to_discipline(discipline, field)
        parent_ids = discipline_subjects.filter(parent__isnull=False).values('parent_id').distinct()
        for parent in self.filter(pk__in=parent_ids):
            tree.append({
                'parent': parent,
                # 'children': parent.subject_set.belonging_to_discipline(discipline, field).all()
                'children': self.filter(parent=parent).filter(pk__in=discipline_subjects.values('id'))
            })
        return tree


class Discipline(CommonModel):

    class Meta(CommonModel.Meta):
        verbose_name = u'דיסיפלינה'
        verbose_name_plural = u'דיסיפלינות'


class DesignerManager(GenericManager):
    def specializing_in(self, discipline):
        result = []
        for designer in Designer.objects.all():
            if designer.main_discipline() == discipline:
                result.append(designer)
        return result


class Designer(CommonModel):

    def main_discipline(self):
        try:
            key = self.work_set.values('discipline').annotate(dcount=Count('discipline')).order_by('-dcount')[0]['discipline']
        except IndexError:
            return None
        return Discipline.objects.get(id=key)
    main_discipline.short_description = u'תחום עיצוב עיקרי'

    def work_count(self):
        return self.work_set.count()
    work_count.short_description = u'מספר עבודות'

    objects = DesignerManager()

    photo = models.ImageField(u'תמונת מעצב', upload_to="images/", blank=True)
    birth_year = models.IntegerField(u'שנת לידה', blank=True, null=True)
    death_year = models.IntegerField(u'שנת מוות', blank=True, null=True)
    birth_country = models.ForeignKey("Country", verbose_name="מדינת לידה", default=None, null=True)
    philosophy_summary = models.TextField(u'תקציר פילוסופיה', blank=True)
    philosophy = models.FileField(u'קובץ פילוסופיה', upload_to="pdf/", blank=True)
    is_active = models.BooleanField(u'פעיל/ה', default=False)
    generation = models.ForeignKey("Generation", verbose_name="שייך לדור", null=True)

    class Meta(CommonModel.Meta):
        verbose_name = "מעצב"
        verbose_name_plural = "מעצבים"


class WorkManager(models.Manager):
    def one_from_each_discipline(self):
        works = []
        for discipline in Discipline.objects.all():
            try:
                works.append(discipline.work_set.order_by('?')[0])
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

    sidar_id = models.CharField(u'קוד עבודה', max_length=50, null=True, unique=True)
    designer = models.ForeignKey('Designer', verbose_name=u'מעצב', null=True)
    raw_image = models.ImageField(u'תמונת מקור', upload_to='works', null=True)
    fullscale_image = ImageSpecField(processors=[ResizeToFit(width=600), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    midsize_image = ImageSpecField(processors=[ResizeToFit(width=350), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    preview_image = ImageSpecField(processors=[ResizeToFit(width=100), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    subjects = models.ManyToManyField("Subject", verbose_name=u'נושאים', null=True)
    discipline = models.ForeignKey("Discipline", verbose_name=u'תחום עיצוב', null=True)
    category = models.ForeignKey("Category", verbose_name=u'קטגוריה', null=True)
    # Date related fields
    publish_date_as_text = models.CharField(u'תאריך כמלל', max_length=50, blank=True, null=True)
    publish_date = models.DateField(verbose_name="תאריך הוצאה לאור", null=True)
    date_accuracy_level = models.CharField(u'רמת דיוק תאריך', max_length=2, choices=DATE_ACCURACY_LEVELS, default=None, blank=True)
    # Size related fields
    size_as_text = models.CharField(u'גודל כמלל', max_length=50, blank=True, null=True)
    height = models.DecimalField(u'גובה', max_digits=5, decimal_places=2, default=0)
    width = models.DecimalField(u'רוחב', max_digits=5, decimal_places=2, default=0)
    depth = models.DecimalField(u'עומק (תלת-מימדי)', max_digits=5, decimal_places=2, default=0)

    client = models.ForeignKey('Client', verbose_name=u'לקוח', null=True)
    techniques = models.ManyToManyField('Technique', verbose_name=u'טכניקות')
    collections = models.ManyToManyField('Collection', verbose_name=u'מאוספים')
    keywords = models.ManyToManyField('Keyword', verbose_name=u'מילות מפתח')
    description = models.TextField(u'תיאור')
    country = models.ForeignKey("Country", verbose_name=u'מדינה', null=True, blank=True)

    class Meta(CommonModel.Meta):
        verbose_name = "עבודה"
        verbose_name_plural = "עבודות"

    def __unicode__(self):
        return self.sidar_id


class Country(CommonModel):
    class Meta(CommonModel.Meta):
        verbose_name = "מדינה"
        verbose_name_plural = "מדינות"


class Category(CommonModel):

    parent = models.ForeignKey('self', verbose_name=u'קטגורית על', blank=True, null=True)
    objects = GenericManager()

    class Meta(CommonModel.Meta):
        verbose_name = "קטגוריה"
        verbose_name_plural = "קטגוריות"


class Client(CommonModel):

    class Meta(CommonModel.Meta):
        verbose_name = "לקוח"
        verbose_name_plural = "לקוחות"


class Technique(CommonModel):

    class Meta(CommonModel.Meta):
        verbose_name = "טכניקה"
        verbose_name_plural = "טכניקות"


class Collection(CommonModel):
    homepage = models.URLField(u'אתר בית')

    class Meta(CommonModel.Meta):
        verbose_name = "אוסף"
        verbose_name_plural = "אוספים"


class Keyword(CommonModel):
    class Meta(CommonModel.Meta):
        verbose_name = u'מילת מפתח'
        verbose_name_plural = u'מילות מפתח'


class Subject(CommonModel):
    objects = GenericManager()
    parent = models.ForeignKey('self', verbose_name=u'נושא על', blank=True, null=True)

    class Meta(CommonModel.Meta):
        verbose_name = "נושא"
        verbose_name_plural = "נושאים"


class Generation(CommonModel):

    class Meta(CommonModel.Meta):
        verbose_name = u'דור מעצבים'
        verbose_name_plural = u'דורות מעצבים'
