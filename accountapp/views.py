from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '가입이 완료되었습니다.')
            return HttpResponseRedirect(reverse('mainapp:home'))
        else:
            form = UserCreationForm()
            messages.error(request, '이메일 혹은 비밀번호를 확인해주세요.')
            return render(request, 'accountapp/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'accountapp/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:home'))
        else:
            messages.error(request, '이메일 혹은 비밀번호가 틀렸습니다.')
            return render(request, 'accountapp/login.html')
    else:
        return render(request, 'accountapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('accountapp:login'))