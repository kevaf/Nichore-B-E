from django.shortcuts import render
from .models import ArtGallery, Profile
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import ArtGallerySerializer
# Create your views here.

class ArtGalleryList(APIView):
    def get(self, request, format=None):
        all_art = ArtGallery.objects.all()
        serializers = ArtGallerySerializer(all_art, many= True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ArtGallerySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

