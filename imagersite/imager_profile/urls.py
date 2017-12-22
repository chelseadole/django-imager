"""Urls for profiles."""

from django.conf.urls import url
from imager_profile.views import ProfileView, AltProfileView, EditProfileView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(ProfileView.as_view()), name='profile'),
    url(r'^edit/$', login_required(EditProfileView.as_view()), name='edit_profile'),
    url(r'^(?P<slug>\w+\d*)/$', AltProfileView.as_view(), name="alt_profile")
]
