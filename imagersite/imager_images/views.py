"""Imager image views."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from imager_images.forms import NewAlbum, NewPhoto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class LibraryView(LoginRequiredMixin, ListView):
    """Library view displays all photo and album views."""

    login_url = '/login'
    template_name = 'imagersite/library.html'
    model = User

    def get_queryset(self, user=None):
        """Get queryset for photos."""
        return User


class AlbumGalleryView(ListView):
    """Gallery of all public albums."""

    template_name = "imagersite/album_gallery.html"
    model = Album
    exclude = []

    def get_context_data(self):
        """Context data for AlbumGallery."""
        queryset = Album.objects.filter(published="Public")
        albums = queryset.all()
        album_pages = Paginator(albums, 4)
        return {
            "albums": album_pages.page(int(self.request.GET['page']))
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
        photo_pages = Paginator(photos, 4)
        return {
            "photos": photo_pages
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


class AddAlbumView(LoginRequiredMixin, CreateView):
    """Create a new album."""

    model = Album
    login_url = '/login'
    template_name = "imagersite/add_album.html"
    success_url = '/images/library'
    form_class = NewAlbum

    def post(self, request, *args, **kwargs):
        """Post info for new album."""
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.instance.user = self.request.user
            return self.form_valid(form)
        return self.form_invalid(form)


class AddPhotoView(LoginRequiredMixin, CreateView):
    """Create a new image."""

    model = Photo
    login_url = '/login'
    template_name = "imagersite/add_photo.html"
    success_url = '/images/library'
    form_class = NewPhoto

    def post(self, request, *args, **kwargs):
        """Post info for new photo."""
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.instance.user = self.request.user
            return self.form_valid(form)
        return self.form_invalid(form)


class EditPhoto(LoginRequiredMixin, UpdateView):
    """Edit a photo."""

    model = Photo
    login_url = '/login'
    template_name = 'imagersite/edit_photo.html'
    success_url = '/images/library'
    fields = ['title', 'img', 'description', 'published']


class EditAlbum(LoginRequiredMixin, UpdateView):
    """Edit an album."""

    model = Album
    login_url = '/login'
    template_name = 'imagersite/edit_album.html'
    success_url = '/images/library'
    fields = ['title', 'cover', 'photos', 'description', 'published']
