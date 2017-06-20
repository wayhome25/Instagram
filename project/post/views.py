from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })

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
