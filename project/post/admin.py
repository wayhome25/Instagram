from django import forms
from django.forms import Textarea
from django.contrib import admin
from .models import Post, Tag, Like


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = '__all__'

class LikeInline(admin.TabularInline):
    model = Post.like_user_set.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    list_display_links = ['author', 'nickname', 'content']
    form = PostForm
    inlines = [LikeInline,]

    def nickname(request, post):
        return post.author.profile.nickname

    list_select_related = ['author__profile']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']
