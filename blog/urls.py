# app blog URL Configuration

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>/', views.blog_detail, name='blog_detail'),
    path(
        'category/<int:category_pk>/',
        views.blog_with_category,
        name='blog_with_category'),
]