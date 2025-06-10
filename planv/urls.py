from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createUser/', views.create_user, name="create_user"),
]
