from django.shortcuts import render
from .models import ArtGallery, Profile
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import ArtGallerySerializer
# Create your views here.

class ArtGalleryList(generics.GenericAPIView):
    def get(self, request, format=None):
        all_art = ArtGallery.objects.all()
        serializers = ArtGallerySerializer(all_art, many= True)
        return Response(serializers.data)
