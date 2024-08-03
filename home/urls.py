from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('abc/', views.abc),
]
