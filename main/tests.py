from django.test import TestCase
from django.urls import resolve
from main import views


class HomeTest(TestCase):

    def test_root_url_resolver_to_home_view(self):
        resolved_view = resolve('/')
        self.assertEqual(views.home, resolved_view.func)
