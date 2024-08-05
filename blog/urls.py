from . import views
from django.urls import path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('posts/', views.posts, name='posts'),
    path('<int:post_id>/', views.post, name='post'),

]
