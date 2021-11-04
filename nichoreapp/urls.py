from django.conf.urls import url
from . import views
from django.urls import path
from .views import RegisterAPI, LoginAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from knox import views as knox_views



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[

   url(r'^api/all-art/$', views.ArtGalleryList.as_view()),
   url(r'api/all-art/art-id/(?P<pk>[0-9]+)/$', views.ArtGalleryDets.as_view()),
   url(r'^api/profiles/$', views.ProfileList.as_view()),
   url(r'api/profiles/profile-id/(?P<pk>[0-9]+)/$', views.ProfileDets.as_view()),
   path('api/register/', RegisterAPI.as_view(), name='register'),
   path('api/login/', LoginAPI.as_view(), name='login'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),

   path('', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]