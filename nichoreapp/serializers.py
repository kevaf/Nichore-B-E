from rest_framework import serializers
from .models import ArtGallery, Profile
from django.contrib.auth.models import User

class ArtGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtGallery
        fields = ('title', 'artist', 'price', 'pub_date')