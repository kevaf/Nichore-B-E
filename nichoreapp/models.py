from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

class ArtGallery(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='art')
    price = models.IntegerField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class Profile(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(max_length=254, blank=True)
    profile_picture = CloudinaryField('image')
    artwork = models.ForeignKey(ArtGallery, on_delete=models.SET_NULL, null=True, related_name='work', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()