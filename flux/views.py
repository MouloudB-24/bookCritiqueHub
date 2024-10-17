from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class HomePage(LoginRequiredMixin, View):
    template_name = 'flux/home.html'
    login_url = 'login'

    def get(self, request):
        return render(request, self.template_name)
