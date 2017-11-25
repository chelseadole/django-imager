"""Define the Photo and Album model classes."""

from django.db import models
from django.contrib.auth.models import User


PUBLISH = (
    ('Private', 'Private'),
    ('Shared', 'Shared'),
    ('Public', 'Public'),
)


class Photo(models.Model):
    """Define the Photo class."""

    title = models.CharField(
        max_length=50,
        unique=True)
    description = models.CharField(
        max_length=200)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = PUBLISH
    user = models.OneToOneField(
        User
    )


class Album(models.Model):
    """Define the Album class."""

    photos = []
    title = models.CharField(
        max_length=50, unique=True)
    description = models.CharField(
        max_length=200, unique=True)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = PUBLISH
    cover = models.CharField(
        max_length=50)
    user = models.OneToOneField(
        User
    )
