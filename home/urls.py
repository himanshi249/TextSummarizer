from django.contrib import admin
from django.urls import path, include
from home import views 

urlpatterns = [
    path('homepage', views.home, name='home'),
    path('summarize', views.sumry, name='sumry'), 
]