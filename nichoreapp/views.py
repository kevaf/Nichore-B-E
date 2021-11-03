from django.shortcuts import render
from  django.http import Http404
from .models import ArtGallery, Profile
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import ArtGallerySerializer, ProfileSerializer

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

class ArtGalleryDets(APIView):

    def get_art(self, pk):
        try:
            return ArtGallery.objects.get(pk=pk)
        except ArtGallery.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        art = self.get_art(pk)
        serializers = ArtGallerySerializer(art)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        art = self.get_art(pk)
        serializers = ArtGallerySerializer(art, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        art = self.get_art(pk)
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many= True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)