# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.processors.crop import TrimBorderColor
# from django.utils.translation import ugettext_lazy as _
from utils import nullify
from django.db.models import Count


class CommonModel(models.Model):
    name = models.CharField(u'שם', max_length=50)
    # add last updated

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Discipline(CommonModel):

    class Meta:
        verbose_name = u'דיסיפלינה'
        verbose_name_plural = u'דיסיפלינות'


class Designer(CommonModel):

    @classmethod
    def from_portfolio(cls, portfolio_row):
        name_he = portfolio_row[u'מעצב'].replace('\'', '`')
        return Designer.objects.get(name_he=name_he)

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

    photo = models.ImageField(u'תמונת מעצב', upload_to="images/", blank=True)
    # birth_year = models.DateField(u'שנת לידה', blank=True, null=True)
    birth_year = models.IntegerField(u'שנת לידה', blank=True, null=True)
    # death_year = models.DateField(u'שנת מוות', blank=True, null=True)
    death_year = models.IntegerField(u'שנת מוות', blank=True, null=True)
    birth_country = models.ForeignKey("Country", verbose_name="מדינת לידה", default=None, null=True)
    philosophy_summary = models.TextField(u'תקציר פילוסופיה', blank=True)
    philosophy = models.FileField(u'קובץ פילוסופיה', upload_to="pdf/", blank=True)
    is_active = models.BooleanField(u'פעיל/ה')
    generation = models.ForeignKey("Generation", verbose_name="שייך לדור")

    class Meta:
        verbose_name = "מעצב"
        verbose_name_plural = "מעצבים"


class Work(CommonModel):
    sidar_id = models.CharField(u'קוד עבודה', max_length=50, null=True, unique=True)
    # designer = models.ForeignKey('Designer', verbose_name=u'מעצב', null=True)
    raw_image = models.ImageField(u'תמונת מקור', upload_to='works', null=True)
    fullscale_image = ImageSpecField(processors=[ResizeToFit(width=600), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    midsize_image = ImageSpecField(processors=[ResizeToFit(width=350), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    preview_image = ImageSpecField(processors=[ResizeToFit(width=100), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    # subjects = models.ManyToManyField("Subject", verbose_name=u'נושאים')
    discipline = models.ForeignKey("Discipline", verbose_name=u'תחום עיצוב', null=True)
    # category = models.ForeignKey("Category", verbose_name=u'קטגוריה')
    # publish_date       = models.DateField(verbose_name="תאריך הוצאה לאור")
    # publish_date_as_text = models.CharField(u'תאריך כמלל', max_length=50, blank=True, null=True)
    # client = models.ForeignKey("Client", verbose_name=u'לקוח')
    # technique = models.ForeignKey("Technique", verbose_name=u'טכניקה')
    # height             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="גובה")
    # width              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="רוחב")
    # size_as_text = models.CharField(u'גודל כמלל', max_length=50, blank=True, null=True)
    description = models.TextField(u'תיאור')
    # country = models.ForeignKey("Country", verbose_name=u'מדינה')
    # collection = models.ForeignKey("Collection", verbose_name=u'מאוסף')

    class Meta:
        verbose_name = "עבודה"
        verbose_name_plural = "עבודות"

    def __unicode__(self):
        return self.sidar_id


class Country(CommonModel):
    @classmethod
    def from_portfolio(cls, portfolio_row):
        return Country.objects.get_or_create(name_he=nullify(portfolio_row[u'ארץ']),
                                             name_en=nullify(portfolio_row[u'Country']))[0]
    # unique

    class Meta:
        verbose_name = "מדינה"
        verbose_name_plural = "מדינות"


class Category(CommonModel):
    @classmethod
    def from_portfolio(cls, portfolio_row):
        u"""
        >>> cat = Category.from_portfolio({u'קטגוריה': u'Art and Design אמנות ועיצוב'})
        >>> cat.name_he == u'אמנות ועיצוב' and cat.name_en == 'Art and Design'
        True
        """
        from utils import has_hebrew_chars
        name_en = []
        name_he = []
        for word in portfolio_row[u'קטגוריה'].split(' '):
            if has_hebrew_chars(word):
                name_he.append(word)
            else:
                name_en.append(word)
        return Category.objects.get_or_create(name_he=nullify(' '.join(name_he)), defaults={'name_en': nullify(' '.join(name_en))})[0]

    parent = models.ForeignKey('self', verbose_name="קטגורית על", blank=True, null=True)

    class Meta:
        verbose_name = "קטגוריה"
        verbose_name_plural = "קטגוריות"


class Client(CommonModel):

    @classmethod
    def from_portfolio(cls, portfolio_row):
        return Client.objects.get_or_create(name_he=nullify(portfolio_row[u'לקוח']),
                                            name_en=nullify(portfolio_row['Client']))[0]

    class Meta:
        verbose_name = "לקוח"
        verbose_name_plural = "לקוחות"


class Technique(CommonModel):

    @classmethod
    def from_portfolio(cls, portfolio_row):
        return Technique.objects.get_or_create(
            name_he=nullify(portfolio_row[u'טכניקה']),
            name_en=nullify(portfolio_row['Technique']))[0]

    class Meta:
        verbose_name = "טכניקה"
        verbose_name_plural = "טכניקות"


class Collection(CommonModel):
    homepage = models.URLField(u'אתר בית')

    class Meta:
        verbose_name = "אוסף"
        verbose_name_plural = "אוספים"


class Subject(CommonModel):

    @classmethod
    def from_portfolio(cls, portfolio_row):
        return [(Subject.objects.get_or_create(name_he=nullify(subject.strip())))[0] for subject in portfolio_row[u'נושא'].split(',')]

    class Meta:
        verbose_name = "נושא"
        verbose_name_plural = "נושאים"


class Generation(CommonModel):

    class Meta:
        verbose_name = u'דור מעצבים'
        verbose_name_plural = u'דורות מעצבים'
