from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from bookcritique.settings import LOGIN_REDIRECT_URL
from . import forms


class TicketView(LoginRequiredMixin, View):
    template_name = 'posts/ticket.html'
    form_class = forms.TicketForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect(LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={'form': form})

