from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geo'),
    path('skills', views.skills)
]