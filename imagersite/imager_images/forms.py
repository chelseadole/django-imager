"""Forms outline for creating new Album and Photo object."""

from django import forms
from imager_images.models import Album, Photo


class NewAlbum(forms.ModelForm):
    """New Album."""

    class Meta:
        """Album metadata."""

        model = Album
        exclude = []


class NewPhoto(forms.ModelForm):
    """New Photo."""

    class Meta:
        """Album metadata."""

        model = Photo
        exclude = []
