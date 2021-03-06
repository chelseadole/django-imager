"""Test module for imagersite."""
from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.core import mail
from bs4 import BeautifulSoup as soup
from django.contrib.auth.models import User
import factory


# from imagersite.views import HomeView


class FactoryUserBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'NewThing{}3'.format(user))
    email = factory.Sequence(lambda user: '{}@codefellows.edu'.format(user))


class ViewTests(TestCase):
    """Testing views and routing."""

    def setUp(self):
        """Set up."""
        self.client = Client()

        user = FactoryUserBoi.create()
        user.set_password('percentsignbois')
        user.save()
        self.user = user

    def test_home_view(self):
        """Test that HomeView loads."""
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_has_no_username_without_login(self):
        """Test that when you go to Home without being logged in, there is no personalized welcome."""
        response = self.client.get(reverse_lazy('home'))
        parsed = soup(response.content, 'html.parser')
        self.assertTrue('Welcome, ' not in parsed)

    def test_home_view_retrieves_correct_template(self):
        """Test that when homeview loads, it loads to base.html."""
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_login_loads_with_get_request_to_page(self):
        """Test that when one loads the login page, it works."""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_loads_error_with_incorrect_user(self):
        """Test that the login view gives error page with wrong user."""
        login_attempt = {'username': 'thewronglogin', 'password': 'thewrongpassword'}
        response = self.client.post('/login/', login_attempt)
        page_html = soup(response.content, 'html.parser')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTrue("Please enter a correct username and password. Note that both fields may be case-sensitive." in str(page_html))

    def test_library_view_retrieves_correct_template(self):
        """Test that when libraryview loads, it loads to library.html."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        self.assertTemplateUsed(response, 'imagersite/library.html')

    def test_library_view_has_correct_content(self):
        """Test that when you go to Home without being logged in, the correct template comes through."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        parsed = soup(response.content, 'html.parser')
        self.assertTrue('Albums' in str(parsed))
