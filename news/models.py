# news/models.py

from django.db import models
from django.utils.text import slugify
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        original_slug = slugify(self.name)
        unique_slug = original_slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(original_slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        original_slug = slugify(self.name)
        unique_slug = original_slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(original_slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.name

class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = News.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass  # when new photo then we do nothing, normal case

        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(News, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        original_slug = slugify(self.title)
        unique_slug = original_slug
        num = 1
        while News.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(original_slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.title
