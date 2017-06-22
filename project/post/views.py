from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.objects.prefetch_related('tag_set').select_related('author__profile').all()

    if request.method == 'POST' :
        tag = request.POST.get('tag')
        tag_clean = ''.join(e for e in tag if e.isalnum()) #특수문자 삭제
        return redirect('post:post_search', tag_clean)

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
            messages.info(request, '새 글이 등록되었습니다.')
            return redirect('post:post_list')

    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {
        'form': form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.tag_set.all().delete()
            post.tag_save()
            messages.success(request, '수정완료')
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
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')
    else:
        post.delete()
        messages.success(request, '삭제완료')
        return redirect('post:post_list')

def post_search(request, tag):
    post_list = Post.objects.filter(tag_set__name__icontains=tag)
    return render(request, 'post/post_search.html', {
        'tag': tag,
        'post_list': post_list,
    })
