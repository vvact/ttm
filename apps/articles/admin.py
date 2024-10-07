from django.contrib import admin
from .models import Article

# Customize the Article Admin Interface
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author','title', 'category', 'slug', 'status')
    search_fields = ('title', 'author__username')  
    prepopulated_fields = {'slug': ('title',)}

    # Optional: If you want to specify which fields to show in the form
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'category', 'author', 'status')
        }),
    )

# Register the Article model and the custom admin class
admin.site.register(Article, ArticleAdmin)
