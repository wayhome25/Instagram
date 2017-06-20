from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_save()
            return redirect('post:post_list')

    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {
        'form': form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.tag_set.all().delete()
            post.tag_save()
            return redirect('post:post_list')

    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {
        'form': form,
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post:post_list')
    else:
        post.delete()
        return redirect('post:post_list')
