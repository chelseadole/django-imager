"""Tests for Album and Photo models."""
from django.test import TestCase

from imager_images.models import Album, Photo
from django.contrib.auth.models import User
import factory
import os
from imagersite.settings import BASE_DIR
from datetime import datetime


class FactoryUserBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'NewThing{}3'.format(user))
    email = factory.Sequence(lambda user: '{}@codefellows.gov'.format(user))


class FactoryPhotoBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = Photo

    title = 'my photo title'
    description = 'wow what a great photo'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'Public'
    # user = FactoryUserBoi.create()


class PhotoAndAlbumTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        self.photos = []
        user = FactoryUserBoi.create()
        user.set_password('percentsignbois')
        user.save()

        user.profile.location = "Seattle"
        user.profile.save()

        users_album = Album(user=user, title="Albumerino", published="Public")
        users_album.save()

        for i in range(10):
            photo = FactoryPhotoBoi.build()
            photo.user = user
            photo.save()
            users_album.photos.add(photo)
            self.photos.append(photo)

        self.album = users_album
        self.profile = user.profile
        self.user = user

    # Profile tests below

    def test_profile_exists_on_user(self):
        """Test profile was created and has Seattle location."""
        self.assertTrue(self.profile is not None)

    def test_profile_location_is_seattle(self):
        """Test profile location has been set to Seattle."""
        self.assertEqual(self.profile.location, "Seattle")

    # Photo tests below

    def test_num_photos_created(self):
        """Test the number of photo objects made by the Boi."""
        self.assertTrue(len(self.photos) == 10)

    def test_photo_has_correct_title_attribute_when_created(self):
        """Test that a created user has correct title attribute."""
        self.assertEqual(self.photos[0].title, "my photo title")

    def test_photo_user_exists(self):
        """Test that Photo has user."""
        self.assertTrue(self.user is not None)

    def test_new_photo_user_has_correct_email(self):
        """Ensure that a new photo is properly connected by checking email."""
        self.assertTrue("@codefellows.gov" in self.user.email)
        self.assertEqual(self.user, self.album.user)

    # Album Tests below

    def test_album_boi_made_albums(self):
        """Test utility of FactoryBoi."""
        albums = [self.album]
        self.assertTrue(len(albums) == 1)

    def test_album_has_correct_title_attribute_when_created(self):
        """Test that a created user has correct title attribute."""
        self.assertEqual(self.album.title, "Albumerino")

    def test_album_has_correct_published_attribute_when_initialized(self):
        """Test that a created user has correct published attribute."""
        self.assertEqual(self.album.published, "Public")

    def test_album_has_user(self):
        """Test that Album class has a user."""
        self.assertTrue(self.album.user is not None)

    def test_album_has_user_and_user_has_attributes(self):
        """Test that Album class has a user."""
        self.assertTrue("codefellows.gov" in self.album.user.email)

    def tearDown(self):
        """Tear down testing."""
        delete_1 = os.path.join(BASE_DIR + 'imager_images', 'confusables.json')
        delete_2 = os.path.join(BASE_DIR + 'imager_images', 'categories.json')
        os.system('rm ' + delete_1)
        os.system('rm ' + delete_2)
