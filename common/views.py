from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from .models import People

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            usernamed = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            usere = authenticate(username=usernamed, password=raw_password)  
            p=People(name=str(usernamed))
            p.save()
            # 사용자 인증
            login(request, usere )  # 로그인
            
            return redirect('main:screen')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})



