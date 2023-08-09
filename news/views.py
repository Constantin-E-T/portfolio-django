# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import News, Category, Tag
from django.core.paginator import Paginator


def news_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news_list = News.objects.all().order_by('-created_at')
    latest_news = News.objects.order_by('-created_at')[:5]  # Get the 5 latest news articles
    tags = Tag.objects.all()  # Get all tags
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news_list = news_list.filter(category=category)
    
    paginator = Paginator(news_list, 3)  # Show 5 news per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {'category': category, 'categories': categories, 'news': news, 'latest_news': latest_news, 'tags': tags})




def news_detail(request, id, slug):
    news = get_object_or_404(News, id=id, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})

def news_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    news_list = News.objects.filter(tags=tag).order_by('-created_at')
    categories = Category.objects.all()
    latest_news = News.objects.order_by('-created_at')[:5]
    tags = Tag.objects.all()

    paginator = Paginator(news_list, 3)  # Show 1 news per page for demonstration
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    context = {
        'news': news,
        'categories': categories,
        'latest_news': latest_news,
        'tags': tags
    }
    return render(request, 'news/news_list.html', context)





