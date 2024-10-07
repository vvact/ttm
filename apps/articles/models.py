from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from apps.categories.models import Category  # Import Category model

from nanoid import generate

def generate_nanoid():
    # Generate a 4-character NanoID
    return generate(size=4)

# Article Model
class Article(models.Model):
    id = models.CharField(max_length=4, primary_key=True, default=generate_nanoid, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('Draft', 'Draft'), ('Published', 'Published')])

    def save(self, *args, **kwargs):
        # Generate slug based on title
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1

        while Article.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1

        self.slug = slug  # Override slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

