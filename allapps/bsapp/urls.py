from django.urls import path
from . import views


app_name = 'bsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_language/', views.add_language, name='add_language'),
    path('add_framework/', views.add_framework, name='add_framework'),
]
