"""Profile views."""

from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from django.views.generic import DetailView, ListView, UpdateView


class ProfileView(ListView):
    """View for user profile page."""

    model = User
    template_name = "imagersite/profile.html"

    def get_context_data(self, **kwargs):
        """Context data for user stats."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        if user.username == '':
            context = {"logged_in": False}
        else:
            prof_object = user.profile
            albums_pub = Album.objects.filter(user=user, published="Public").count()
            albums_pri = Album.objects.filter(user=user, published="Private").count()
            photos_pub = Photo.objects.filter(user=user, published="Public").count()
            photos_pri = Photo.objects.filter(user=user, published="Public").count()
            context = {
                "logged_in": True,
                "user": user,
                "profile": prof_object,
                "public_albums": albums_pub,
                "private_albums": albums_pri,
                "photos_pub": photos_pub,
                "photos_pri": photos_pri
            }
        return context


class AltProfileView(DetailView):
    """View for non-user profile."""

    model = User
    template_name = "imagersite/altprofile.html"
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        """Context data for alt profile."""
        try:
            context = super(AltProfileView, self).get_context_data(**kwargs)
            user_object = User.objects.get(username=self.kwargs['slug'])
            profile_object = user_object.profile
            context = {
                "user_exists": True,
                "user": user_object,
                "profile": profile_object
            }
            return context
        except User.DoesNotExist:
            return {'user_exists': False}


class EditProfileView(UpdateView):
    """View to edit profile information based on User and Profile models."""

    model = User
    template = "imagersite/edit_profile.html"
    success_url = "/profile"
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        """Context data for user stats."""
        context = super(EditProfileView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        return {
            "user": user,
            "profile": user.profile,
        }
