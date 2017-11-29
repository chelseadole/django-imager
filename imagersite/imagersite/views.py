"""Views for Django Imager."""

from django.shortcuts import render
from registration.backends.hmac.views import RegistrationView
from imager_profile.models import Profile
from imager_images.models import Album, Photo
from django.contrib.auth.models import User


def home_view(request, number=None):
    """View for the home page."""
    login_context = {}
    if request.user.username:
        login_context = {"username": request.user.username}
    return render(request, 'imagersite/home.html', context=login_context)


def login_view(request):
    """View for login."""
    return render(request, 'imagersite/login.html', context={})


def logout_view(request):
    """View for logout."""
    return render(request, 'imagersite/logout.html', context={})


def register_view(request):
    """View for registration."""
    return render(request, 'imagersite/register.html', context={})


def profile_view(request):
    """View for profile."""
    if request.user.username == '':
        return render(request, 'imagersite/profile.html', context={"logged_in": False})
    else:
        user_object = User.objects.get(username=request.user.username)
        profile_object = Profile.objects.get(user=user_object)
        profile_context_dict = {
            "logged_in": True,
            "user": user_object,
            "profile": profile_object
        }
        return render(request, 'imagersite/profile.html', context=profile_context_dict)


def alt_profile_view(request):
    """View for non-user profile."""
    try:
        user_object = User.objects.get(username=request.path[1:])
    except User.DoesNotExist:
        return render(request, 'imagersite/altprofile.html', context={"user_exists": False})
    profile_object = Profile.objects.get(user=user_object)
    alt_profile_context_dict = {
        "user_exists": True,
        "user": user_object,
        "profile": profile_object
    }
    return render(request, 'imagersite/altprofile.html', context=alt_profile_context_dict)
