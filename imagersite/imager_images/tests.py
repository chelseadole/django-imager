"""Tests for Album and Photo models."""
from django.test import TestCase

from imager_images.models import Album, Photo
from django.contrib.auth.models import User
import factory
from datetime import datetime
from django.test import Client
from django.urls import reverse_lazy
from imager_images.forms import NewAlbum, NewPhoto
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings

client = Client()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = settings.MEDIA_ROOT
media = os.path.join(MEDIA_ROOT)
os.system('mv ' + media + '/images/ ' + media + '/saved_images//')
os.system('mv ' + media + '/cover-images/ ' + media + '/saved_cover-images//')


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
    img = SimpleUploadedFile(
        name='sample_meme.jpg',
        content=open(os.path.join(BASE_DIR,
                                  'imagersite',
                                  'static',
                                  'sample_meme.jpg',
                                  ), 'rb').read(),
        content_type='image/jpeg'
    )
    description = 'wow what a great photo'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'Public'


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

        cover_img = SimpleUploadedFile(
            name='sample_meme.jpg',
            content=open(os.path.join(BASE_DIR,
                                      'imagersite',
                                      'static',
                                      'sample_meme.jpg',
                                      ), 'rb').read(),
            content_type='image/jpeg'
        )
        users_album = Album(user=user, title="Albumerino", published="Public", cover=cover_img)
        users_album.save()

        for i in range(10):
            photo = FactoryPhotoBoi.build()
            photo.user = user
            photo.save()
            users_album.photos.add(photo)
            users_album.save()
            self.photos.append(photo)

        self.album = users_album
        self.profile = user.profile
        self.user = user

    # Profile tests below

    def tearDown(self):
        """Tear down testing data."""
        os.system('rm -rf ' + media + '/images/')
        os.system('rm -rf ' + media + '/cover-images/')

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


class ImageViewTests(TestCase):
    """Tests for imager_profile/views.py."""

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

    def tearDown(self):
        """Tear down testing data."""
        os.system('rm -rf ' + media + '/images/')
        os.system('rm -rf ' + media + '/cover-images/')

    def test_response_code_to_addalbum_page(self):
        """Test that going to add_album gets a 200 Ok response."""
        response = self.client.get(reverse_lazy('add_album'))
        self.assertEqual(response.status_code, 200)

    def test_response_code_to_addphoto_page(self):
        """Test that going to add_photo gets a 200 Ok response."""
        response = self.client.get(reverse_lazy('add_photo'))
        self.assertEqual(response.status_code, 200)

    def test_response_code_to_photogallery_page(self):
        """Test that going to add_photo gets a 200 Ok response."""
        response = self.client.get(reverse_lazy('photo_gallery'))
        self.assertEqual(response.status_code, 200)

    def test_response_code_to_albumgallery_page(self):
        """Test that going to add_photo gets a 200 Ok response."""
        response = self.client.get(reverse_lazy('album_gallery'))
        self.assertEqual(response.status_code, 200)

    def test_response_code_to_library_page(self):
        """Test that going to add_photo gets a 200 Ok response."""
        response = self.client.get(reverse_lazy('library'))
        self.assertEqual(response.status_code, 200)

    def test_incorrectly_formatted_use_of_photo_form(self):
        """Test that a post request to add_photo works."""
        new_photo = {
            'description': 'the boy of the photos',
            'published': "Private"
        }
        form = NewPhoto(data=new_photo)
        self.assertFalse(form.is_valid())

    # def test_correctly_formatted_use_of_photo_form(self):
    #     """Test that adding all fields to photo form works."""
    #     new_photo = {
    #         'description': 'the boy of the photos',
    #         'published': "Private",
    #         'title': 'this time it will work!'
    #     }
    #     form = NewPhoto(data=new_photo)
    #     self.assertTrue(form.is_valid())

    def test_incorrectly_formatted_use_of_album_form(self):
        """Test that a bad use of add_photo doesnt work."""
        new_album = {
            'description': 'the boy of the photos',
            'thiscategoryisincorrect': 'nope'
        }
        form = NewAlbum(data=new_album)
        self.assertFalse(form.is_valid())

    # def test_correctly_formatted_use_of_album_form(self):
    #     """Test that a valid use of add_album works."""
    #     new_album = {
    #         'description': 'the boy of the photos',
    #         'title': 'a working album',
    #         'published': 'Private',
    #         'photos': '2',
    #         'cover': None
    #     }
    #     form = NewAlbum(data=new_album)
    #     self.assertTrue(form.is_valid())

    def test_detail_view_wont_work_for_nonexisting_photo(self):
        """Test a detail view for a photo whose ID doesnt exist."""
        response = self.client.get(reverse_lazy('photo_view'), args=[100])
        self.assertEqual(response.status_code, 404)

    # def test_album_gallery_only_shows_public_albums(self):
    #     """Test that album_gallery url only shows public view albums."""
    #     response = self.client.get(reverse_lazy('album_gallery'))
    #     parsed_page = soup(response.content, 'html.parser')
    #     # Assert that every listed album here is "Public"

