"""Profile views."""

from django.shortcuts import render
from django.contrib.auth.models import User
from imager_profile.models import Profile
from imager_images.models import Photo, Album
from django.views.generic import DetailView


class ProfileView(DetailView):
    """View for user profile page."""

    model = User
    template_name = "imagersite/profile.html"

    def get_context_data(self, **kwargs):
        """Context data for user stats."""
        if not kwargs:
            context = {"logged_in": False}
        else:
            user_object = User.objects.get(username=request.user.username)
            prof_object = user_object.profile
            albums_pub = Album.objects.filter(user=user_object, published="Public").count()
            albums_pri = Album.objects.filter(user=user_object, published="Private").count()
            photos = Photo.objects.filter(user=user_object).count()
            context = {
                "logged_in": True,
                "user": user_object,
                "profile": prof_object,
                "public_albums": albums_pub,
                "private_albums": albums_pri,
                "total_photos": photos
            }
        return context


class AltProfileView(DetailView):
    """View for non-user profile."""

    model = User
    template_name = "imagersite/altprofile.html"

    def get_context_data(self, user):
        """Context data for alt profile."""
        try:
            user_object = User.objects.get(username=user)
            profile_object = user_object.profile
            context = {
                "user_exists": True,
                "user": user_object,
                "profile": profile_object
            }
            return context
        except User.DoesNotExist:
            return {"user_exists": False}
