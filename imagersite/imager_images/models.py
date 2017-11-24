"""Define the Photo and Album model classes."""

from django.db import models


class Photo(models.Model):
    """Define the Photo class."""

    title = models.CharField(
        max_length=50)
    description = models.CharField(
        max_length=200)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
