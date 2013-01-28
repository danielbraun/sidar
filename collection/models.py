from django.db import models
from backoffice.models import Work
from django.contrib.auth.models import User
from positions import PositionField


class Collectable(models.Model):
    original_work = models.ForeignKey(Work)
    comments = models.TextField()
    position = PositionField(collection='user')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['position']

    def move_up(self):
        self.position -= 1
        self.save()

    def move_down(self):
        self.position += 1
        self.save()
