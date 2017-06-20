from django import forms
from django.forms import Textarea
from django.contrib import admin
from .models import Post, Tag


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'created_at']
    list_display_links = ['author', 'content']
    form = PostForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
