from django.contrib import admin
from .models import Category


# Customize the Category Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Register the Category model and the custom admin class
admin.site.register(Category, CategoryAdmin)



