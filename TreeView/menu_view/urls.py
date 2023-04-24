from django.contrib.auth import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', test),
]
