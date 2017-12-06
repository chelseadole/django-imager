"""Various tests for our models."""

from django.test import TestCase
from imager_profile.models import Profile
from django.contrib.auth.models import User
from imager_profile.forms import EditProfileForm
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
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
        test_user.profile = example
        self.assertEqual(example.website, "www.chelseadole.com")
        self.assertEqual(test_user.profile.website, "www.chelseadole.com")
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
        test_user2.profile = example2
        self.assertEqual(example2.camera, "Canon")
        self.assertEqual(test_user2.profile.camera, "Canon")
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


class EditProfileTests(TestCase):
    """Tests for Editing Profile view."""

    def setUp(self):
        """Generate users using Factory Boiiii."""
        test_users = [FactoryUserBoi.create() for i in range(20)]

        for user in test_users:
            user.set_password('ultimatepotato')
            user.save()

        self.users = test_users

    def test_new_profile_has_no_website_unless_added(self):
        """Test that generated profile has no contents upon User init."""
        test = self.users[0]
        self.assertEqual(test.profile.website, '')

    def test_new_profile_has_no_bio_unless_added(self):
        """Test that generated profile has no contents upon User init."""
        test = self.users[0]
        self.assertEqual(test.profile.bio, '')

    def test_new_profile_has_no_camera_unless_added(self):
        """Test that generated profile has no contents upon User init."""
        test = self.users[0]
        self.assertEqual(test.profile.camera, '')

    def test_new_profile_page_loads(self):
        """Test profile page loads."""
        response = self.client.get(reverse_lazy('profile'))
        self.assertEqual(response.status_code, 302)

    def test_response_code_to_edit_profile_page(self):
        """Test GET request to edit profile."""
        response = self.client.get(reverse_lazy('edit_profile'))
        self.assertEqual(response.status_code, 302)

    def test_template_used_on_edit_profile(self):
        """Test Template used."""
        self.client.force_login(self.users[4])
        response = self.client.get("/profile/edit")
        self.assertTemplateUsed(response, 'imagersite/profile_form.html')

    def test_post_request_to_edit_album(self):
        """Test POST request to edit profile."""
        self.client.force_login(self.users[5])
        resubmitted_prof = {
            "website": "https://www.google.com",
            "location": "West Siberia",
            "fee": 30.00,
            "camera": "Nikon",
            "services": "Other",
            "bio": "mybio",
            "phone": 2069141111,
            "Username": "newuser",
            "Email": "otherbaaab@baab.gov"
        }
        request = self.client.post('/profile/edit', resubmitted_prof)
        self.assertEqual(request.status_code, 302)
        updated = Profile.objects.get(user=self.users[5])
        self.assertEqual(updated.fee, 30.00)
        self.assertEqual(updated.services, "Other")
        self.assertEqual(updated.user.username, 'newuser')
