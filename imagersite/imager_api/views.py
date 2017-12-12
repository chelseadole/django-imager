
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin


class APIView(LoginRequiredMixin, generics.ListAPIView):
    """."""
    login_url = '/login'
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
