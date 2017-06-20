from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'created_at']
    list_display_links = ['author', 'content']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
