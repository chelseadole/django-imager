"""Forms outline for creating new Album and Photo object."""

from django import forms
from imager_images.models import Album, Photo


class NewAlbum(forms.ModelForm):
    """New Album."""

    # def __init__(self, *args, **kwargs):
    #     super(SuccessfulFeedbackForm, self).__init__(*args, **kwargs)
    #     self.fields['was_satisifed'].initial = True

    class Meta:
        """Album metadata."""

        model = Album
        exclude = ['photos', 'date_uploaded', 'date_modified', 'date_published', 'user']


class NewPhoto(forms.ModelForm):
    """New Photo."""

    class Meta:
        """Album metadata."""

        model = Photo
        exclude = ["date_published", "user"]
