from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="YRC HOME"),
    path('tracker/', views.tracker, name="YRC TRACKER"),
    path('clients/', views.clients, name="YRC CLIENTS"),
    path('gallery/', views.gallery, name="YRC GALLERY"),
    path('about/', views.about, name="YRC ABOUT"),
    path('contact/', views.contact, name="YRC CONTACT"),
    path('login/', views.login, name="YRC LOGIN"),
]
