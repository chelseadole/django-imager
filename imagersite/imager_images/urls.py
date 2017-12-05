"""Urls for images."""

from django.conf.urls import url
from imager_images.views import LibraryView, PhotoGalleryView, AlbumGalleryView, PhotoView, AlbumView, AddAlbumView, AddPhotoView, EditPhoto, EditAlbum

urlpatterns = [
    url(r'^library$', LibraryView.as_view(), name="library"),
    url(r'^photos$', PhotoGalleryView.as_view(), name="photo_gallery"),
    url(r'^albums$', AlbumGalleryView.as_view(), name="album_gallery"),
    url(r'^albums/add$', AddAlbumView.as_view(), name="add_album"),
    url(r'^photos/add$', AddPhotoView.as_view(), name="add_photo"),
    url(r'^photos/(?P<pk>\d+)/edit$', EditPhoto.as_view(), name="edit_photo"),
    url(r'^albums/(?P<pk>\d+)/edit$', EditAlbum.as_view(), name="edit_album"),
    url(r'^photos/(?P<pk>\d+)$', PhotoView.as_view(), name="photo_view"),
    url(r'^albums/(?P<pk>\d+)$', AlbumView.as_view(), name="album_view")
]
