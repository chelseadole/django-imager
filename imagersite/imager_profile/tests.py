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

    def test_profile_has_website():
        """Test that the profile class has the website attribute."""