from django.contrib import admin
from django.urls import path
#장고 함수인 path와 blog 애플리케이션에서 사용할 모든 views를 import함
from . import views

urlpatterns = [
    path('', views.post_list, name='post_index'),
    path('list', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name ='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
]