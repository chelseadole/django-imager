"""Views for Django Imager."""

from django.shortcuts import render
from registration.backends.hmac.views import RegistrationView


def home_view(request, number=None):
    """View for the home page."""
    return render(request, 'imagersite/home.html', context={})


def login_view(request):
    """View for login."""
    return render(request, 'imagersite/login.html', context={})


def logout_view(request):
    """View for logout."""
    return render(request, 'imagersite/logout.html', context={})


def register_view(request):
    """View for registration."""
    return render(request, 'imagersite/register.html', context={})
