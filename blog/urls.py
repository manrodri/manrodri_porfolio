from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='blog'),
    path('<int:blog_id>', views.show_blog, name='show_blog'),
]