"""Serializers for Imager API."""

from imagersite.imager_images import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Photo" Serializer model."""

    class Meta:
        """Metadata."""
        model = Photo
        fields = ('title', 'img', 'description', 'date_uploaded', 'published')
