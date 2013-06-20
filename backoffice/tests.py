# -*- coding: utf-8 -*-
from django.test import TestCase

from backoffice.management.commands.import_portfolio import match_is_self_collected, match_collector, match_technique
from backoffice.models import Discipline
from bibliography.models import BookCategory
from django.core.urlresolvers import reverse
from backoffice.models import Collector
from backoffice.models import Work
from django.core.files import File


class ViewTests(TestCase):

    def assertResponseOK(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def setUp(self):
        Discipline(name_en='g', active=True).save()

    def test_about_page(self):
        self.assertResponseOK('/discipline/1/about/')

    def test_homepage(self):
        self.assertResponseOK('/')

    def test_discipline_homepage(self):
        self.assertResponseOK('/discipline/1/')

    def test_book_list(self):
        self.assertResponseOK('/discipline/1/book/')

    def test_book_list_with_category(self):
        BookCategory(pk=1).save()
        response = self.assertResponseOK('/discipline/1/book/1/')
        self.assertIn('category', response.context)

    def test_category_list(self):
        self.assertResponseOK('/discipline/1/category/')

    def test_subject_list(self):
        self.assertResponseOK('/discipline/1/subject/')

    def test_designer_list(self):
        self.assertResponseOK('/discipline/1/designer/')

    def test_article_list(self):
        self.assertResponseOK('/discipline/1/article/')

    def test_video_list(self):
        self.assertResponseOK('/discipline/1/video/')

    def test_event_list(self):
        self.assertResponseOK('/discipline/1/event/')

    def test_search_page_loads(self):
        self.assertResponseOK('/discipline/1/search/')


class ManagementCommandTests(TestCase):
    def test_match_is_self_collected(self):
        self.assertEqual(
            match_is_self_collected(u'ריזינגר דן', u'ריזינגר דן'),
            True)
        self.assertEqual(
            match_is_self_collected(u'גרוס עלי', u'עלי גרוס'),
            True)
        self.assertEqual(
            match_is_self_collected(u'ריזינגר דן', u'מאוסף ריזינגר דן'),
            True)
        self.assertEqual(
            match_is_self_collected(u'האחים שמיר', u'ציונות 2000'),
            False)

    def test_match_collector(self):
        self.assertEqual(
            match_collector(u'האחים שמיר',
                            u'ציונות 2000')[0].name_he, u'ציונות 2000')
        self.assertEqual(match_collector(u'ריזינגר דן', u'ריזינגר דן'), [])

    def test_match_technique(self):
        self.assertEqual(match_technique(u'תלת מימד&#44; קינטיקה'),
                         u'תלת מימד, קינטיקה')


class WorkListViewTests(TestCase):
    def setUp(self):
        self.discipline = Discipline.objects.create(name_en='g', active=True)
        self.collector = Collector.objects.create()
        self.work = Work.objects.create(discipline=self.discipline)
        self.work_with_a_collector = Work.objects.create(discipline=self.discipline)
        self.work_with_a_collector.of_collections.add(self.collector)
        self.collector_response = self.client.get(
            reverse('work-list',
                    kwargs={'discipline': self.discipline.id,
                            'collector': self.collector.id})
        )

    def test_browse_by_collector(self):
        """It should be possible to browse the works a of a collector."""
        self.assertEqual(self.collector_response.status_code, 200)
        self.assertIn(self.work_with_a_collector,
                      self.collector_response.context['object_list'])

    def test_filter_by_collector(self):
        """It should display only the selected collector's works."""
        self.assertNotIn(self.work,
                         self.collector_response.context['object_list'])


class WorkTests(TestCase):
    def test_sidar_id_change_after_upload(self):
        """After Uploading a new image, the Work's sidar_id should update
           accordingly, excluding the file's extension."""
        work = Work.objects.create()
        self.assertEqual(work.sidar_id, '')
        work.raw_image = File(open('static/img/test_image.jpg'))
        work.save()
        self.assertEqual(work.sidar_id, 'test_image')
