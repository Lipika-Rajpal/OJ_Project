from django.contrib import admin
from django.urls import path, include
from judge import views
app_name = 'judge'
urlpatterns = [

    path('', views.problems, name = 'problem'),
    path('problems/<int:problem_id>/',views.problem_detail, name = 'problem_detail'  )
]
