from . import views
from django.urls import path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('posts/', views.posts, name='posts'),
]
