from django.contrib import admin
from .models import Post, CategoryTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'image', 'image_thumb')


@admin.register(CategoryTag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
