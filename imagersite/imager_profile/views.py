"""Profile views."""

from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from imager_profile.models import Profile
from django.views.generic import DetailView, ListView, UpdateView
from imager_profile.forms import EditProfileForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class ProfileView(ListView):
    """View for user profile page."""

    model = User
    template_name = "imagersite/profile.html"

    def get_context_data(self, **kwargs):
        """Context data for user stats."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        prof_object = user.profile
        albums_pub = Album.objects.filter(user=user, published="Public").count()
        albums_pri = Album.objects.filter(user=user, published="Private").count()
        photos_pub = Photo.objects.filter(user=user, published="Public").count()
        photos_pri = Photo.objects.filter(user=user, published="Public").count()
        return {
            "user": user,
            "profile": prof_object,
            "public_albums": albums_pub,
            "private_albums": albums_pri,
            "photos_pub": photos_pub,
            "photos_pri": photos_pri
        }


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

    model = Profile
    template = "imagersite/profile_form.html"
    success_url = reverse_lazy('profile')
    form_class = EditProfileForm
    # fields = []

    def get_object(self):
        """Overwriting UpdateView object to get user."""
        return self.request.user.profile

    def form_valid(self):
        """Check that form is valid and successful before editing."""
        return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     """Context data for user stats."""
    #     context = super(EditProfileView, self).get_context_data(**kwargs)
    #     user = context['view'].request.user
    #     return {
    #         "user": user,
    #         "profile": user.profile
    #     }
