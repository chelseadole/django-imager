"""Imager image views."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView, CreateView
from django import forms


class LibraryView(ListView):
    """Library of user's albums."""

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


class PhotoView(DetailView):
    """Detail view of one photo."""

    template_name = "imagersite/photo_detail.html"
    model = Photo


class AlbumView(ListView):
    """Detail view of one album and its photos."""

    template_name = "imagersite/album_detail.html"
    model = Album

    def get_context_data(self, **kwargs):
        """Context data for Album view."""
        queryset = Album.objects.filter(id=self.kwargs['pk'])
        album = queryset.get()

        return {
            'album': album
        }


class AddAlbumView(CreateView):
    """Create a new album."""

    model = Album
    template_name = "imagersite/add_album.html"
    fields = ["title", "description", "cover", "published"]
    success_url = 'library'

    def post(self, request, *args, **kwargs):
        """Post info for new album."""
        import pdb; pdb.set_trace()
        form = self.get_form()
        # form.user = request.user.id
        if form.is_valid():
            form.user_id = request.user.id
            return self.form_valid(form)
        return self.form_invalid(form)


class AddPhotoView(CreateView):
    """Create a new image."""

    model = Photo
    template_name = "imagersite/add_photo.html"
    fields = ["title", "description", "img", "published"]
    success_url = 'library'

    def post(self, request, *args, **kwargs):
        """Post info for new photo."""
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
