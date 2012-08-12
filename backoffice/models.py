# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.utils.translation import ugettext_lazy as _

class CommonModel(models.Model):
	name = models.CharField(verbose_name='שם', max_length=50)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		abstract = True


class Discipline(CommonModel):
	class Meta:

		verbose_name = "מחלקה"
		verbose_name_plural = "מחלקות"

class Designer(CommonModel):
	photo         = models.ImageField(verbose_name="תמונת מעצב", upload_to="/designer_portraits")
	birth_date    = models.DateField(verbose_name="תאריך לידה")
	death_date    = models.DateField(verbose_name="תאריך מוות")
	birth_country = models.ForeignKey("Country", verbose_name="מדינת לידה")
	philosophy    = models.TextField(verbose_name="פילוסופיה")
	is_active     = models.BooleanField(verbose_name="פעיל/ה")
	generation    = models.ForeignKey("Generation", verbose_name="שייך לדור")

	class Meta:
		verbose_name = "מעצב"
		verbose_name_plural = "מעצבים"


class Work(CommonModel):
	raw_image       = models.ImageField(upload_to='works')
	fullscale_image = ImageSpecField(processors=[ResizeToFit(width=600)], image_field='raw_image')
	midsize_image   = ImageSpecField(processors=[ResizeToFit(width=350)], image_field='raw_image')
	preview_image   = ImageSpecField(processors=[ResizeToFit(width=100)], image_field='raw_image')
	subjects        = models.ManyToManyField("Subject", verbose_name="נושאים")
	discipline      = models.ForeignKey("Discipline", verbose_name="תחום עיצוב")
	category        = models.ForeignKey("Category", verbose_name="קטגוריה")
	publish_date    = models.DateField(verbose_name="תאריך הוצאה לאור")
	client          = models.ForeignKey("Client", verbose_name="לקוח")
	technique       = models.ForeignKey("Technique", verbose_name="טכניקה")
	height          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="גובה")
	width           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="רוחב")
	description     = models.TextField(verbose_name="תיאור")
	country         = models.ForeignKey("Country", verbose_name="מדינה")
	collection      = models.ForeignKey("Collection", verbose_name="מאוסף")

	class Meta:
		verbose_name = "עבודה"
		verbose_name_plural = "עבודות"

class Country(CommonModel):

	class Meta:
		verbose_name = "מדינה"
		verbose_name_plural = "מדינות"


class Category(CommonModel):
	parent = models.ForeignKey('self', verbose_name="קטגורית על", blank=True, null=True)

	class Meta:
		verbose_name = "קטגוריה"
		verbose_name_plural = "קטגוריות"


class Client(CommonModel):
	
	class Meta:
		verbose_name = "לקוח"
		verbose_name_plural = "לקוחות"


class Technique(CommonModel):

	class Meta:
		verbose_name = "טכניקה"
		verbose_name_plural = "טכניקות"


class Collection(CommonModel):
	
	class Meta:
		verbose_name = "אוסף"
		verbose_name_plural = "אוספים"

class Subject(CommonModel):
	
	class Meta:
		verbose_name = "נושא"
		verbose_name_plural = "נושאים"

class Generation(CommonModel):

	class Meta:
		verbose_name = "דור מעצבים"
		verbose_name_plural = "דורות מעצבים"