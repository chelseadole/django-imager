"""Various tests for our models."""

from django.test import TestCase
from django.db import models
from imager_profile.models import ProfileManager, Profile
from django.contrib.auth.models import User
import factory


class FactoryUserBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'McF{}ace'.format(user))
    email = factory.Sequence(lambda user: '{}@codefellows.gov'.format(user))


class FactoryProfileBoi(factory.django.DjangoModelFactory):
    """Factory for creating test Profile."""

    class Meta:
        """Meta class."""

        model = Profile

    website = "www.yahoo.com"
    fee = 222.22
    camera = "Fujifilm"
    bio = "This is where a bio would be. Happy face."
    phone = 1876543210
    user = FactoryUserBoi()


class ProfileTests(TestCase):
    """Imager Prof."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        test_users = [FactoryProfileBoi.create() for i in range(20)]

        for person in test_users:
            person.user.set_password('percentsignbois')
            person.user.save()

        self.users = test_users

    def test_profile_must_have_created_user_class(self):
        """Test making profile without user."""
        with self.assertRaises(Exception):
            this_will_fail = Profile()
            this_will_fail.save()

    def test_profile_has_attributes_and_is_created(self):
        """Test that a created user has correct attributes."""
        example = Profile.objects.first()
        self.assertEqual(example.website, "www.yahoo.com")
        self.assertEqual(example.user.email, User.objects.first().email)

    def test_user_built_in_adds_new_user(self):
        """User built in class."""
        self.test_user = User(email='chelsea@chelsea.com', username='blerg')
        self.test_profile = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            active=True,
            camera="Canon",
            bio="My bio",
            phone=2069147021,
            user=self.test_user
        )
        all_users = User.objects.all()
        length = len(User.objects.all())
        self.assertEqual(len(all_users), length)
        self.test_user.save()
        self.assertEqual(len(all_users), length + 1)
