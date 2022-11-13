from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('start/', views.index, name='home'),
    path('result/', views.result, name='result')
]
