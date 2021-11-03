from django.contrib import admin
from .models import Profile, ArtGallery

# Register your models here.
admin.site.register(ArtGallery)
admin.site.register(Profile)