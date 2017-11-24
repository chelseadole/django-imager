"""Various tests for our models."""

from django.test import TestCase
from imager_profile.models import Profile
from django.contrib.auth.models import User
import factory


class FactoryUserBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'McF{}ace'.format(user))
    email = factory.Sequence(lambda user: '{}@codefellows.gov'.format(user))


class ProfileTests(TestCase):
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

    def test_new_profile_isnt_active(self):
        """Ensure that a new profile is inactive."""
        test_user = User.objects.first()
        example = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            camera="Canon",
            bio="My bio",
            phone=1069147021,
            user=test_user
        )
        self.assertFalse(example.is_active())
