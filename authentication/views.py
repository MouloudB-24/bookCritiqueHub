from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def logout_user(request):
    logout(request)
    return redirect('login')
