"""Urls for images."""

from django.conf.urls import url
from imager_images.views import LibraryView

urlpatterns = [
    url(r'^library$', LibraryView.as_view(), name="library")
]
