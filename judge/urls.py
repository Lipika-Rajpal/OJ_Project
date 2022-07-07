from django.contrib import admin
from django.urls import path, include
from judge import views

urlpatterns = [

    path('judge/', views.index, name = 'problem')
]