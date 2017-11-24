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


class AlbumTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        test_users = [FactoryUserBoi.create() for i in range(20)]
        test_photos = [FactoryPhotoBoi.create() for i in range(200)]
        test_albums = [FactoryAlbumBoi.create() for i in range[60]]
        for user in test_users:
            user.set_password('percentsignbois')
            user.save()

        self.users = test_users
        self.photos = test_photos
        self.albums = test_albums

    def test_profile_must_have_created_user_class(self):
        """Test making profile without user."""
        with self.assertRaises(Exception):
            this_will_fail = Profile(
                website="www.chelseadole.com",
                fee="1.00",
                camera="Canon",
                bio="My bio",
                phone=1069147021,
                user=User()
            )
            this_will_fail.save()

    def test_profile_has_attributes_and_is_created(self):
        """Test that a created user has correct attributes."""
        test_user = User.objects.first()
        example = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user
        )
        self.assertEqual(example.website, "www.chelseadole.com")
        self.assertEqual(example.user.email, User.objects.first().email)

    def test_user_built_in_adds_new_user(self):
        """User built in class."""
        test_user2 = User.objects.last()
        example2 = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user2
        )
        self.assertEqual(example2.camera, "Canon")
        self.assertEqual(example2.user.username, User.objects.last().username)

    def test_new_profile_is_active(self):
        """Ensure that a new profile is active."""
        test_user3 = User.objects.first()
        example = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user3
        )
        self.assertTrue(example.is_active)


class PhotoTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        test_users = [FactoryUserBoi.create() for i in range(20)]

        for user in test_users:
            user.set_password('percentsignbois')
            user.save()

        self.users = test_users

    def test_profile_must_have_created_user_class(self):
        """Test making profile without user."""
        with self.assertRaises(Exception):
            this_will_fail = Profile(
                website="www.chelseadole.com",
                fee="1.00",
                camera="Canon",
                bio="My bio",
                phone=1069147021,
                user=User()
            )
            this_will_fail.save()

    def test_profile_has_attributes_and_is_created(self):
        """Test that a created user has correct attributes."""
        test_user = User.objects.first()
        example = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user
        )
        self.assertEqual(example.website, "www.chelseadole.com")
        self.assertEqual(example.user.email, User.objects.first().email)

    def test_user_built_in_adds_new_user(self):
        """User built in class."""
        test_user2 = User.objects.last()
        example2 = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user2
        )
        self.assertEqual(example2.camera, "Canon")
        self.assertEqual(example2.user.username, User.objects.last().username)

    def test_new_profile_is_active(self):
        """Ensure that a new profile is active."""
        test_user3 = User.objects.first()
        example = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user3
        )
        self.assertTrue(example.is_active)
