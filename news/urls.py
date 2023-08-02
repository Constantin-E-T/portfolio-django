# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('category/<slug:category_slug>/', views.news_list, name='news_list_by_category'),
    path('<int:id>/<slug:slug>/', views.news_detail, name='news_detail'),
    path('tag/<slug:tag_slug>/', views.news_by_tag, name='news_by_tag'),
]
