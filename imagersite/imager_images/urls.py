"""Urls for images."""

from django.conf.urls import url
from imager_images.views import LibraryView, PhotoGalleryView, AlbumGalleryView, PhotoView

urlpatterns = [
    url(r'^library$', LibraryView.as_view(), name="library"),
    url(r'^photos$', PhotoGalleryView.as_view(), name="photo_gallery"),
    url(r'^albums$', AlbumGalleryView.as_view(), name="album_gallery"),
    url(r'^(?P<pk>\d+)$', PhotoView.as_view(), name="photo_view")
    # url(r'^<album_id>$', AlbumView.as_view(), name="album_view")
]
