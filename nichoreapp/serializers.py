from django.db.models import fields
from rest_framework import serializers
from .models import ArtGallery, Profile
from django.contrib.auth.models import User

class ArtGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtGallery
        fields = ('title', 'artist', 'price', 'pub_date')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields = ('user', 'about', 'profile_picture', 'artwork')