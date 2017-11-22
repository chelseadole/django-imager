"""Various tests for our models."""

from django.test import TestCase
from django.db import models
from imager_profile.models import ProfileManager, Profile
from django.contrib.auth.models import User


def sample_profile():
    """A sample profile for use in tests."""
    test = Profile()
    test.website = "www.google.com"
    test.fee = 111.11
    test.active = True
    test.camera = "Sony"
    test.bio = "This is where a bio would be."
    test.phone = 1234567890
    test.user = User()
    return test


sample_profile().save()


class ProfileTests(TestCase):
    """Define the ProfileTests class."""

    def test_profile_has_attributes(self):
        """Test that the profile class has the correct attributes."""
        self.assertEqual(sample_profile().website, "www.google.com")

    def test_new_user_saved_to_db(self):
        """Test that a new user must be saved to db before it can be used."""
        test = Profile()
        test.website = "www.yahoo.com"
        test.fee = 222.22
        test.active = True
        test.camera = "Fujifilm"
        test.bio = "This is where a bio would be. Happy face."
        test.phone = 9876543210
        test.user = User()
        return test

    def test_user_built_in_adds_new_user(self):
        """User built in class."""
        chelsea = User(
            username="dolewhippp",
            email="chelseadole@gmail.com"
        )
        chelsea_profile = Profile(
            website="www.chelseadole.com",
            fee="1.00",
            active=True,
            camera="Canon",
            bio="My bio",
            phone=2069147021,
            user=self.chelsea
        )
        chelsea.save()
        all_users = User.objects.all()
        self.assertEqual(len(all_users), 1)
        # self.assertEquals(self.chelsea, chelsea)
