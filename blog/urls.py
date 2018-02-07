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
    path('<int:blog_pk>/md', views.blog_detail_md, name='blog_detail_md'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
]
