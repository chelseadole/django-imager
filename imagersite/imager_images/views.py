"""Imager image views."""

from django.shortcuts import render
from imager_images.models import Album, Photo
from django.views.generic import ListView
from django.contrib.auth.models import User


class LibraryView(ListView):
    """."""
    template_name = "imagersite/library.html"
    model = Album
    exclude = []

#     def get_context_data(self, user):
#         """Context data for Library."""
#         try:
#             user_object = User.objects.get(username=request)

# try:
#         user_object = User.objects.get(username=user)
#         profile_object = user_object.profile
#         context = {
#             "user_exists": True,
#             "user": user_object,
#             "profile": profile_object
#         }
#         return render(request, 'imagersite/altprofile.html', context=context)
#     except User.DoesNotExist:
#         return render(request, 'imagersite/altprofile.html', context={"user_exists": False})
