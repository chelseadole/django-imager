"""Serializers for Imager API."""

from imager_images.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    """Photo" Serializer model."""

    class Meta:
        """Metadata."""
        model = Photo
        fields = ('title', 'img', 'description', 'date_uploaded', 'published')
