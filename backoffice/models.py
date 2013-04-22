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
    info = models.TextField(u'מידע על הדיסיפלינה')
    active = models.BooleanField(u'פעיל')

    def work_count(self):
        return self.work_set.count()
    work_count.short_description = u'מספר עבודות'

    def short_name(self):
        return u'ע.' + self.name

    def long_name(self):
        return u'עיצוב ' + self.name

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
    death_year = models.IntegerField(u'שנת מוות', blank=True, null=True)
    birth_country = models.ForeignKey("Country", verbose_name="מדינת לידה", default=None, null=True)
    philosophy_summary = models.TextField(u'תקציר פילוסופיה', blank=True)
    philosophy = models.FileField(u'קובץ פילוסופיה', upload_to="pdf/", blank=True)
    is_active = models.BooleanField(u'פעיל/ה', default=False)

    class Meta(CommonModel.Meta):
        verbose_name = "מעצב"
        verbose_name_plural = "מעצבים"


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
    tags = TaggableManager()

    sidar_id = models.CharField(u'קוד עבודה', max_length=50, null=True, unique=True, blank=True)
    designer = models.ForeignKey('Designer', verbose_name=u'מעצב', null=True)
    raw_image = models.ImageField(u'תמונת מקור', upload_to='works', null=True)
    processed_image = ImageSpecField(
        processors=[ResizeToFit(width=350), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    # fullscale_image = ImageSpecField(
    #     processors=[ResizeToFit(width=600), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    # midsize_image = ImageSpecField(
    #     processors=[ResizeToFit(width=350), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    # preview_image = ImageSpecField(
    #     processors=[ResizeToFit(width=100), TrimBorderColor(sides=('t', 'r', 'b', 'l'))], image_field='raw_image')
    subjects = models.ManyToManyField("Subject", verbose_name=u'נושאים', null=True)
    discipline = models.ForeignKey("Discipline", verbose_name=u'תחום', null=True)
    category = models.ForeignKey("Category", verbose_name=u'קטגוריה', null=True)
    # Date related fields
    publish_date_as_text = models.CharField(u'תאריך כמלל', max_length=50, blank=True, null=True)
    # publish_date = models.DateField(verbose_name="תאריך הוצאה לאור", null=True)
    # date_accuracy_level = models.CharField(u'רמת דיוק תאריך', max_length=2,
    # choices=DATE_ACCURACY_LEVELS, default=None, blank=True)
    publish_year = models.IntegerField('שנה', null=True, blank=True, help_text=u'שנה לועזית')
    # Size related fields
    size_as_text = models.CharField(u'גודל כמלל', max_length=128, blank=True, null=True)
    height = models.DecimalField(u'גובה', max_digits=5, decimal_places=2, default=0)
    width = models.DecimalField(u'רוחב', max_digits=5, decimal_places=2, default=0)
    depth = models.DecimalField(u'עומק', max_digits=5, decimal_places=2, default=0)

    client = models.ForeignKey('Client', verbose_name=u'לקוח', null=True)
    country = models.ForeignKey("Country", verbose_name=u'מדינה', null=True, blank=True)
    techniques = models.ManyToManyField('Technique', verbose_name=u'טכניקות', blank=True)
    collections = models.ManyToManyField('Collection', verbose_name=u'מאוספים', blank=True)

    description = models.TextField(u'תיאור')

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


class Country(CommonModel):
    class Meta(CommonModel.Meta):
        verbose_name = "מדינה"
        verbose_name_plural = "מדינות"


class Category(CommonModel, FilterableByDesignerMixin):
    info = models.TextField(u'מידע על הקטגוריה')
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


class Subject(CommonModel, FilterableByDesignerMixin):
    info = models.TextField(u'מידע על הנושא')
    objects = GenericManager()
    parent = models.ForeignKey('self', verbose_name=u'נושא על', blank=True, null=True)

    class Meta(CommonModel.Meta):
        verbose_name = "נושא"
        verbose_name_plural = "נושאים"


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
