from django.contrib.auth import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<slug:slug>/', Menu.as_view(), name='treenode'),
]
