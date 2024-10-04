from django.contrib import admin
from .models import Article,Category
from django.utils.text import slugify

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'category', 'author', 'thumbnail', 'slug','created_at', 'published_at')
    readonly_fields = ('slug', 'created_at') 
    exclude = () 
    list_display = ('title', 'id', 'author', 'created_at', 'published_at')

    def save_model(self, request, obj, form, change):
        if not change:  # If the object is being created
            obj.slug = slugify(obj.title)  # Generate the slug here if the article is new
        super().save_model(request, obj, form, change)

# Register the Article model
admin.site.register(Article, ArticleAdmin)
# Register the Category model
admin.site.register(Category)



