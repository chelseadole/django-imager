"""Views for Django Imager."""

from django.shortcuts import render


def home_view(request, number=None):
    """View for the home page."""
    # template = loader.get_template('lending_library/home.html')
    # response_body = template.render({"potato": number})
    return render(request, 'imagersite/templates/imagersite/home.html', context={})


def login_view(request):
    """View for login."""
    return render(request, 'imagersite/templates/imagersite/login.html', context={})


def logout_view(request):
    """View for logout."""
    return render(request, 'imagersite/templates/imagersite/logout.html', context={})


def register_view(request):
    """View for registration."""
    return render(request, 'imagersite/templates/imagersite/register.html', context={})
