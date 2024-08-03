from . import views
from django.urls import path


urlpatterns = [
    path('', views.blog),
    path('posts/', views.posts),
]
