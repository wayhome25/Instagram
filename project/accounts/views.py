from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import Profile

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
