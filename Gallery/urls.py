from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_posts, name='gallery_posts'),
]
