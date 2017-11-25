"""Tests for Album and Photo models."""

from django.test import TestCase
from imager_images.models import Album, Photo
from django.contrib.auth.models import User
import factory
from datetime import datetime


class FactoryUserBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'McF{}ace'.format(user))
    email = factory.Sequence(lambda user: '{}@codefellows.gov'.format(user))


class FactoryAlbumBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Albums."""

    class Meta:
        """Meta class."""

        model = Album

    title = 'My album title'
    description = 'blargyblarg'
    date_uploaded = datetime.date(2017, 10, 1)
    date_modified = datetime.now()
    date_published = datetime.date(2017, 10, 5)
    published = 'Public'
    cover = 2  # user goes here
    user = FactoryUserBoi()


class FactoryPhotoBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = Photo

    title = 'my photo title'
    description = 'wow what a great photo'
    date_uploaded = datetime.date(2017, 10, 1)
    date_modified = datetime.now()
    date_published = datetime.date(2017, 10, 5)
    published = 'Public'
    user = FactoryUserBoi()


class PhotoTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        # test_users = [FactoryUserBoi.create() for i in range(20)]
        # for user in test_users:
        #     user.set_password('percentsignbois')
        #     user.save()

        test_photos = [FactoryPhotoBoi.create() for i in range(20)]
        # test_albums = [FactoryAlbumBoi.create() for i in range[2]]
        for photo in test_photos:
            user = FactoryUserBoi.create()
            photo.user = user
            # if i % 2 == 0:
            #     test_albums[i].user = user
            photo.user.set_password('percentsignbois')
            user.save()

        # self.users = test_users
        self.photos = test_photos
        # self.albums = test_albums

    def test_photo_has_correct_title_attribute_when_created(self):
        """Test that a created user has correct title attribute."""
        test_user = User.objects.first()
        example = Photo(
            title='mytitle',
            description='description',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 11, 1),
            published='Public',
            user=test_user
        )
        self.assertEqual(example.title, "mytitle")

    def test_photo_has_correct_published_attribute_when_initialized(self):
        """Test that a created user has correct published attribute."""
        test_user = User.objects.first()
        example = Photo(
            title='yeee',
            description='OWOWOWOWW',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Private',
            user=test_user
        )
        self.assertEqual(example.published, "Private")

    def test_user_built_in_adds_new_user(self):
        """User built in class."""
        test_user2 = User.objects.last()
        example2 = Photo(
            title='yeee',
            description='OWOWOWOWW',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Private',
            user=test_user2
        )
        self.assertEqual(str(example2.date_uploaded), '2017-01-01')

    def test_new_photo_user_has_correct_email(self):
        """Ensure that a new photo is properly connected by checking email."""
        photo_owner = FactoryUserBoi.create()
        example2 = Photo(
            title='thenewesttitle',
            description='thenewestdescription',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Private',
            user=photo_owner
        )
        self.assertTrue(example2.user.email.includes('@codefellows.gov'))


class AlbumTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users and albums using Factory Boiiii."""
        test_albums = [FactoryPhotoBoi.create() for i in range(20)]
        for album in test_albums:
            user = FactoryUserBoi.create()
            album.user = user

            album.user.set_password('percentsignbois')
            user.save()

        self.albums = test_albums

    def test_album_has_correct_title_attribute_when_created(self):
        """Test that a created user has correct title attribute."""
        test_user = User.objects.first()
        example = Album(
            title='mytitle',
            description='description',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 11, 1),
            published='Public',
            cover='my cover',
            user=test_user
        )
        self.assertEqual(example.title, "description")

    def test_album_has_correct_published_attribute_when_initialized(self):
        """Test that a created user has correct published attribute."""
        test_user = User.objects.first()
        example = Album(
            title='yeee',
            description='OWOWOWOWW',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Shared',
            cover='my cover',
            user=test_user
        )
        self.assertEqual(example.published, "Shared")

    def test_album_has_correct_cover_attr(self):
        """Test that a created user has cover name attr."""
        test_user = User.objects.first()
        example = Album(
            title='yeee',
            description='OWOWOWOWW',
            date_uploaded=datetime.date(2017, 1, 1),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Shared',
            cover='my cover',
            user=test_user
        )
        self.assertEqual(example.cover, "my cover")

    def test_datetime_is_working_correctly(self):
        """User built in dattime of user works."""
        test_user2 = User.objects.last()
        example2 = Photo(
            title='yeee',
            description='OWOWOWOWW',
            date_uploaded=datetime.date(2017, 3, 20),
            date_modified=datetime.now(),
            date_published=datetime.date(2017, 10, 1),
            published='Private',
            user=test_user2
        )
        self.assertEqual(str(example2.date_uploaded), '2017-03-20')
