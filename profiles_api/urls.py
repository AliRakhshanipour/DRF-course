from django.urls import path, include
from django.contrib import admin
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path('login/', views.UserLoginViewSet.as_view()),
    path('', include(router.urls))
]
