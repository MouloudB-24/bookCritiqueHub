from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from . import forms


def logout_user(request):
    logout(request)
    return redirect('login')


def login_user(request):
    form = forms.LoginForm()
    message = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalide!'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})
