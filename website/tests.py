from django.test import TestCase
from django.test.client import Client


class WebsiteViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
