from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns=[
    url(r'^api/all-art/$', views.ArtGalleryList.as_view()),
    url(r'api/all-art/art-id/(?P<pk>[0-9]+)/$', views.ArtGalleryDets.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),

]