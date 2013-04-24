# -*- coding: utf-8 -*-

from django.db import models
from backoffice.models import Discipline


class Event(models.Model):
    discipline = models.ForeignKey(Discipline, verbose_name=u'תחום עיצוב', blank=True, null=True)
    year = models.IntegerField(u'שנה')
    description = models.CharField(u'תיאור', max_length=255)

    HISTORICAL = 'HIS'
    DESIGN = 'DES'
    DISCIPLINE = 'DIS'

    TYPE_CHOICES = (
        (HISTORICAL, u'הסטורי'),
        (DESIGN, u'עיצוב'),
        (DISCIPLINE, u'תחום עיצוב'),
    )
    type = models.CharField(u'סוג אירוע', max_length=3, choices=TYPE_CHOICES, default=HISTORICAL)
    is_important = models.BooleanField(u'חשוב?')

    def get_decade(self):
        return self.year - self.year % 10

    def save(self, *args, **kwargs):
        if self.type != self.DISCIPLINE:
            self.discipline = None
        return super(Event, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'אירוע הסטורי'
        verbose_name_plural = u'אירועים הסטוריים'
        ordering = ('year',)

    def __unicode__(self):
        return self.description
