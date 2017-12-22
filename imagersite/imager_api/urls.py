"""Imagersite URL Configuration."""

from django.conf.urls import url
from imager_api.views import APIView


urlpatterns = [
    url(r'^$', APIView.as_view(), name="api")
]
