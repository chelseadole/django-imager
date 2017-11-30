"""."""
from django.contrib import admin

# Register your models here.
from imager_images.models import Album, Photo
from imager_profile.models import Profile

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Profile)
