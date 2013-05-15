# -*- coding: utf-8 -*-
from django.test import TestCase
from backoffice.models import Discipline
from bibliography.models import BookCategory
from backoffice.management.commands.import_portfolio import match_is_self_collected
from backoffice.management.commands.import_portfolio import match_collector
from backoffice.management.commands.import_portfolio import match_technique


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

    def test_link_list(self):
        self.assertResponseOK('/discipline/1/link/')

    def test_video_list(self):
        self.assertResponseOK('/discipline/1/video/')

    def test_event_list(self):
        self.assertResponseOK('/discipline/1/event/')

    def test_search_page_loads(self):
        self.assertResponseOK('/discipline/1/search/')


class ManagementCommandTests(TestCase):
    def test_match_is_self_collected(self):
        self.assertEqual(match_is_self_collected(u'ריזינגר דן', u'ריזינגר דן'), True)
        self.assertEqual(match_is_self_collected(u'גרוס עלי', u'עלי גרוס'), True)
        self.assertEqual(match_is_self_collected(u'ריזינגר דן', u'מאוסף ריזינגר דן'), True)
        self.assertEqual(match_is_self_collected(u'האחים שמיר', u'ציונות 2000'), False)

    def test_match_collector(self):
        self.assertEqual(
            match_collector(u'האחים שמיר',
                            u'ציונות 2000')[0].name_he, u'ציונות 2000')
        self.assertEqual(match_collector(u'ריזינגר דן', u'ריזינגר דן'), [])

    def test_match_technique(self):
        self.assertEqual(match_technique(u'תלת מימד&#44; קינטיקה'),
                         u'תלת מימד, קינטיקה')
