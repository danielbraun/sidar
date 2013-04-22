from django.db import models
from backoffice.models import Discipline


class Event(models.Model):
    discipline = models.ForeignKey(Discipline, blank=True, null=True)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
