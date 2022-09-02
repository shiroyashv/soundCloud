from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('me', views.UserView, basename='me')

urlpatterns = [
    path('', include(router.urls)),
    path('google/', views.google_auth),
    path('', views.google_login),
]
