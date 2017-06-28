import json
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import SignupForm
from .models import Profile, Relation

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid(): # clean_<필드명> 메소드 호출
            user = form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 정상적으로 변경되었습니다.')
            return redirect('profile')
        else:
            messages.error(request, '오류가 발생하였습니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form,
    })

@login_required
@require_POST
def follow(request):
    from_user = request.user.profile
    pk = request.POST.get('pk')
    to_user = get_object_or_404(Profile, pk=pk)
    relation, created = Relation.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        message =  '팔로우 시작!'
        status = 1
    else:
        relation.delete()
        message =  '팔로우 취소'
        status = 0

    context = {
        'message': message,
        'status': status,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
