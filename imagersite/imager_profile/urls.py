"""Urls for profiles."""

from django.conf.urls import url
from imager_profile.views import ProfileView, AltProfileView, EditProfileView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^edit$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^(?P<slug>\w+\d*)/$', AltProfileView.as_view(), name="alt_profile")
]
