"""Profile model."""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileManager(models.Model):
    """Manager for Profile."""

    def get_queryset(self):
        """Super get_queryset to filter for active users."""
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class Profile(models.Model):
    """Create Profile."""

    CAMERA_CHOICES = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Olympus', 'Olympus'),
        ('Sony', 'Sony'),
        ('Fujifilm', 'Fujifilm')
    )
    SERVICE_CHOICES = (
        ('Port', 'Portrait'),
        ('Wild', 'Wildlife'),
        ('Film', 'Film'),
        ('BW', 'Black & White'),
        ('Other', 'Other')
    )
    # objects = models.ModelManager()
    website = models.URLField()
    location = models.CharField(
        max_length=50)
    fee = models.FloatField(blank=True, null=True)
    active = ProfileManager()
    camera = models.CharField(
        choices=CAMERA_CHOICES,
        max_length=120)
    services = models.CharField(
        choices=SERVICE_CHOICES,
        max_length=300)
    bio = models.CharField(
        max_length=700)
    phone = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    @property
    def is_active(self):
        """Return whether a user is active."""
        return self.user.is_active

    def __repr__(self):
        """Repr method for Profile."""
        return "Website: {}, Location: {}, Fee: {}, Active: {}, Camera: {}, Services: {}, Bio: {}, Phone: {}, User: {}".format(self.website, self.location, self.fee, self.active, self.camera, self.services, self.bio, self.phone, self.user.username)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Receiver to make profile when User is made."""
    if kwargs['created']:
        profile = Profile(user=kwargs['instance'])
        profile.save()
