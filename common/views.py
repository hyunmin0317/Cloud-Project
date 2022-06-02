from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm


# 계정생성
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)