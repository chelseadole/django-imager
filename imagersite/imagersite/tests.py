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

    def test_homeview_retrieves_correct_template(self):
        """Test that when homeview loads, it loads to base.html."""
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_login_loads_with_get_request_to_page(self):
        """Test that when one loads the login page, it works."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_loads_error_with_incorrect_user(self):
        """Test that the login view gives error page with wrong user."""
        login_attempt = {'username': 'thewronglogin', 'password': 'thewrongpassword'}
        response = self.client.post('/accounts/login/', login_attempt)
        page_html = soup(response.content, 'html.parser')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTrue("Please enter a correct username and password. Note that both fields may be case-sensitive." in str(page_html))
