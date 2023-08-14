# portfolio/urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
]
