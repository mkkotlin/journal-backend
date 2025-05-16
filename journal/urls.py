from django.contrib import admin
from django.urls import  path
from .views import TestAuthView

urlpatterns = [
    path('test/', TestAuthView.as_view())
]