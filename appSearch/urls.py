from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search,  name='search'),
    path('googlePlay/', views.googlePlay, name='googlePlay'),
    path('appStore/', views.appStore, name='appStore'),
]
