"""Test module for imagersite."""
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse_lazy
from bs4 import BeautifulSoup as soup
from django.contrib.auth.models import User
from django.core import mail
from imagersite.views import home_view


class ViewTests(TestCase):
    """Testing views and routing."""

    def setUp(self):
        """Set up."""
        self.client = Client()

    def test_home_view(self):
        """Test that HomeView loads."""
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_has_no_username_without_login(self):
        """Test that when you go to Home without being logged in, there is no personalized welcome."""
        response = self.client.get(reverse_lazy('home'))
        parsed = soup(response.content, 'html.parser')
        self.assertTrue('Welcome, ' not in parsed)