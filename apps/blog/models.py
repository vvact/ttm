import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone


import random
import string

def generate_short_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        verbose_name = "Category"
        app_label = "blog"

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.CharField(
        max_length=4, 
        primary_key=True, 
        default=generate_short_id,
        editable=False
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)



    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)  

    class Meta:
        verbose_name_plural = "Articles"
        ordering = ['-published_at']
        verbose_name = "Article"
        app_label = "blog"
        get_latest_by = 'published_at'

    def __str__(self):
        return self.title

