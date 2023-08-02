from django.contrib import admin
from .models import News, Category, Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(News, NewsAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag, TagAdmin)
