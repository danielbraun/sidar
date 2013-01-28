# -*- coding: utf-8 -*-

from django.db import models
from backoffice.models import Discipline


class BookCategory(models.Model):
    name = models.CharField(u'שם הספר', max_length=128)

    class Meta:
        verbose_name = u'קטגורית ספר'
        verbose_name_plural = u'קטגוריות ספרים'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(u'כותרת', max_length=128)
    discipline = models.ForeignKey(Discipline, verbose_name=u'מחלקת עיצוב')
    category = models.ForeignKey(BookCategory, verbose_name=u'קטגוריה')
    comments = models.CharField(u'הערות', max_length=128)
    author_as_text = models.CharField(u'מחבר/עורך/מאייר', max_length=128)
    publication_as_text = models.CharField(u'הוצאה/מקום/שנה', max_length=128)

    class Meta:
        verbose_name = u'ספר'
        verbose_name_plural = u'ספרים'
        ordering = ['title']

    def __unicode__(self):
        return self.title