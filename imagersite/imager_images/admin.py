"""."""
from django.contrib import admin

# Register your models here.
from imagersite.imager_images.models import Album, Photo
from imagersite.imager_profile.models import Profile

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Profile)
