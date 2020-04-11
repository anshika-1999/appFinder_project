from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.keyword,  name='keyword'),
    path('urlkeyword/', views.urlkeyword, name='urlkeyword'),

]
