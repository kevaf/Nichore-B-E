from django.conf.urls import url
from . import views
from django.urls import path
from .views import ArtGalleryList

urlpatterns=[
    url(r'^api/all-art/$', views.ArtGalleryList.as_view()),

]