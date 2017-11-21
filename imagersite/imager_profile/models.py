"""Profile model."""

from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Model):
    """Manager for Profile."""

    def get_queryset(self):
        """Super get_queryset to filter for active users."""
        return super().get_queryset().filter(user__is_active=True)


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

    website = models.URLField()
    location = models.CharField(
        max_length=50)
    fee = models.FloatField()
    active = ProfileManager()
    camera = models.CharField(
        choices=CAMERA_CHOICES,
        max_length=120)
    services = models.CharField(
        choices=SERVICE_CHOICES,
        max_length=300)
    bio = models.CharField(
        max_length=700)
    phone = models.IntegerField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    @property
    def is_active(self):
        """Return whether a user is active."""
        return self.user.is_active
