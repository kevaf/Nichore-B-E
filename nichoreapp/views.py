from django.shortcuts import render
from  django.http import Http404
from .models import ArtGallery, Profile
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import ArtGallerySerializer, ProfileSerializer, UserSerializer, RegisterSerializer

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

class ProfileDets(APIView):

    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)