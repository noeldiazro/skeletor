from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from main import views


class HomeTest(TestCase):

    def test_root_url_resolver_to_home_view(self):
        resolved_view = resolve('/')
        self.assertEqual(views.home, resolved_view.func)

    def test_home_view_returns_correct_html(self):
        request = HttpRequest()
        response = views.home(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.rstrip().endswith('</html>'))

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
