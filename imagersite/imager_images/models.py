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
<<<<<<< HEAD
        max_length=50)
=======
        max_length=50,
        unique=True)
>>>>>>> ebfb47b0d9a69d3c55d66ab4e91413021664241c
    description = models.CharField(
        max_length=200)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = PUBLISH
<<<<<<< HEAD
=======
    user = models.OneToOneField(
        User
    )
>>>>>>> ebfb47b0d9a69d3c55d66ab4e91413021664241c


class Album(models.Model):
    """Define the Album class."""

<<<<<<< HEAD
=======
    photos = []
>>>>>>> ebfb47b0d9a69d3c55d66ab4e91413021664241c
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
