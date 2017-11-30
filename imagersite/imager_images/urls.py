"""Urls for images."""

from django.conf.urls import url
from imager_images.views import LibraryView, PhotoGalleryView, AlbumGalleryView

urlpatterns = [
    url(r'^library$', LibraryView.as_view(), name="library"),
    url(r'^photos$', PhotoGalleryView.as_view(), name="photo_gallery"),
    url(r'^albums$', AlbumGalleryView.as_view(), name="album_gallery")
]
