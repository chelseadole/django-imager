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


class AlbumGalleryView(ListView):
    """Gallery of all public albums."""
    template_name = "imagersite/album_gallery.html"
    model = Album
    exclude = []

    def get_context_data(self):
        """Context data for AlbumGallery."""
        queryset = Album.objects.filter(published="Public")
        albums = queryset.all()
        return {
            "albums": albums
        }


class PhotoGalleryView(ListView):
    """Gallery of all public photos."""
    template_name = "imagersite/photo_gallery.html"
    model = Photo
    exclude = []

    def get_context_data(self):
        """Context data for PhotoGallery."""
        queryset = Photo.objects.filter(published="Public")
        photos = queryset.all()
        return {
            "photos": photos
        }
