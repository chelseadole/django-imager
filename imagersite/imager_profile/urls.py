"""Urls for profiles."""

from django.conf.urls import url
from imager_profile.views import profile_view, alt_profile_view

urlpatterns = [
    url(r'^$', profile_view, name='profile'),
    url(r'^(?P<user>\w+)$', alt_profile_view, name="alt_profile"),
]
