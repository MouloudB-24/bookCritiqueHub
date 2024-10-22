from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from bookcritique.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

from . import forms


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect(LOGIN_REDIRECT_URL)
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutPageView(View):
    def get(self, request):
        logout(request)
        return redirect(LOGIN_URL)


class SignupPageView(View):
    template_name = 'authentication/signup.html'
    form_class = forms.SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={'form': form})


class PasswordChange(PasswordChangeView):
    template_name = 'authentication/password_change_form.html'
    success_url = reverse_lazy('password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'


class UploadProfilePhoto(View):
    template_name = 'authentication/upload_profile_photo.html'

    def get(self, request):
        form = forms.UploadProfilePhotoForm(instance=request.user)
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={'form': form})

