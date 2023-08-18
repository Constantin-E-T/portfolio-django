# news/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News, Category, Tag
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import NewsForm



def news_list(request, category_slug=None):
    category = None
    # Fetch only categories that have associated posts
    categories = Category.objects.annotate(num_posts=Count('news')).filter(num_posts__gt=0)

    news_list = News.objects.all().order_by('-created_at')
    latest_news = News.objects.order_by('-created_at')[:5]  # Get the 5 latest news articles
    # Fetch only tags that have associated posts
    tags = Tag.objects.annotate(num_news=Count('news__id')).filter(num_news__gt=0)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news_list = news_list.filter(category=category)
    
    paginator = Paginator(news_list, 2)  # Show 5 news per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {'category': category, 'categories': categories, 'news': news, 'latest_news': latest_news, 'tags': tags,'news_list': news_list})




def news_detail(request, id, slug):
    news = get_object_or_404(News, id=id, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})

def news_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    news_list = News.objects.filter(tags=tag).order_by('-created_at')
    categories = Category.objects.annotate(num_posts=Count('news')).filter(num_posts__gt=0)
    latest_news = News.objects.order_by('-created_at')[:5]

    # Fetch only tags that have associated posts
    tags = Tag.objects.annotate(num_news=Count('news__id')).filter(num_news__gt=0)

    paginator = Paginator(news_list, 3)  # Show 3 news per page for demonstration
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    context = {
        'news': news,
        'categories': categories,
        'latest_news': latest_news,
        'tags': tags,
        'selected_tag': tag
    }
    return render(request, 'news/news_list.html', context)

# create update delete post

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, "News article created successfully!")
            return redirect('news_detail', id=news.id, slug=news.slug)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})


def news_edit(request, id, slug):
    news = get_object_or_404(News, id=id, slug=slug)
    
    # Check if the logged-in user is the author of the post
    if request.user != news.author:
        return HttpResponseForbidden("You don't have permission to edit this post.")

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)  # Include request.FILES here
        if form.is_valid():
            form.save()
            messages.success(request, "News article updated successfully!")
            return redirect('news_detail', id=news.id, slug=news.slug)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form})


def news_delete(request, id, slug):
    news = get_object_or_404(News, id=id, slug=slug)
    
    # Check if the logged-in user is the author of the post
    if request.user != news.author:
        return HttpResponseForbidden("You don't have permission to delete this post.")

    news.delete()
    messages.success(request, "News article deleted successfully!")
    return redirect('news_list')






