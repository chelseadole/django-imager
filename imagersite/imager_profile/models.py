from django.db import models

# Create your models here.

class Profile(models.Model):
    """Create Profile."""
    website = models.URLField()
    location = models.CharField(
        max_length=50)
    fee = models.FloatField()
    camera = models.CharField(
        CAMERA_CHOICES=(
            ('Canon', 'Canon'),
            ('Nikon', 'Nikon'),
            ('Olympus', 'Olympus'),
            ('Sony', 'Sony'),
            ('Fujifilm', 'Fujifilm')
        ),
        max_length=120)
    services = models.CharField(
        SERVICE_CHOICES=(
            ('Port', 'Portrait'),
            ('Wild', 'Wildlife'),
            ('Film', 'Film'),
            ('BW', 'Black & White'),
            ('Other', 'Other')
        ),
        max_length=300)
    bio = models.CharField(
        max_length=700)
    phone = models.IntegerField()
    user = 
