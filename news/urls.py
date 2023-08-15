# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('category/<slug:category_slug>/', views.news_list, name='news_list_by_category'),
    path('tag/<slug:tag_slug>/', views.news_by_tag, name='news_by_tag'),
    path('news/<int:id>/<slug:slug>/', views.news_detail, name='news_detail'),
    # create update delete posts
    path('create/', views.news_create, name='news_create'),
    path('<int:id>/<slug:slug>/edit/', views.news_edit, name='news_edit'),
    path('<int:id>/<slug:slug>/delete/', views.news_delete, name='news_delete'),
]
