from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include
from django.urls import path

urlpatterns=[path('polls/',include('polls.urls')),path('admin/',admin.site.urls),]
