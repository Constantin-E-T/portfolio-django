# users/urls.py

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
