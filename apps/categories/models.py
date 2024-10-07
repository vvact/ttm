from django.db import models
from django.utils.text import slugify
import uuid
import hashlib


def generate_short_uuid():
    # Generate a standard UUID
    new_uuid = uuid.uuid4()
    # Hash the UUID and return the first 4 characters of the hash
    return hashlib.sha256(str(new_uuid).encode('utf-8')).hexdigest()[:4]

# Category Model
class Category(models.Model):
    id = models.CharField(max_length=4, primary_key=True, default=generate_short_uuid, editable=False)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate slug based on name
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1

        while Category.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1

        self.slug = slug  # Override slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


    def __str__(self):
        return self.name

