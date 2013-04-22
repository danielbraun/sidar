from django.core.urlresolvers import reverse
from backoffice.models import Discipline
from django.test import TestCase
from .models import Event


class ViewTests(TestCase):
    def setUp(self):
        self.discipline = Discipline.objects.create(name="G")

    def test_event_list(self):
        e1 = Event.objects.create(discipline=self.discipline, year=1950, description='asd')
        e2 = Event.objects.create(year=1968, description='asd')
        response = self.client.get(reverse('timeline_event_list', kwargs={'discipline': self.discipline.id}))
        self.assertEqual(response.context[0], e1)