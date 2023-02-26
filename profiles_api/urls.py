from django.urls import path
from django.contrib import admin
from profiles_api import views

urlpatterns = [
    path('helloApiView/', views.HelloAPiView.as_view())
]
