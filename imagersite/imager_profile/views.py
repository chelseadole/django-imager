"""Profile views."""

from django.shortcuts import render
from django.contrib.auth.models import User
from imager_profile.models import Profile
from imager_images.models import Photo, Album
# Create your views here.


def profile_view(request):
    """View for profile."""
    # import pdb; pdb.set_trace()
    if request.user.username == '':
        context = {"logged_in": False}
    else:
        user_object = User.objects.get(username=request.user.username)
        prof_object = user_object.profile
        albums_pub = Album.objects.filter(user=user_object, published="Public").count()
        albums_pri = Album.objects.filter(user=user_object, published="Private").count()
        photos = Photo.objects.filter(user=user_object).count()
        context = {
            "logged_in": True,
            "user": user_object,
            "profile": prof_object,
            "public_albums": albums_pub,
            "private_albums": albums_pri,
            "total_photos": photos
        }
    return render(request, 'imagersite/profile.html', context=context)


def alt_profile_view(request, user):
    """View for non-user profile."""
    try:
        user_object = User.objects.get(username=user)
        profile_object = user_object.profile
        context = {
            "user_exists": True,
            "user": user_object,
            "profile": profile_object
        }
        return render(request, 'imagersite/altprofile.html', context=context)
    except User.DoesNotExist:
        return render(request, 'imagersite/altprofile.html', context={"user_exists": False})
