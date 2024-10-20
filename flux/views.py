from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from posts.models import Ticket, Review


class HomePage(LoginRequiredMixin, View):
    template_name = 'flux/home.html'
    login_url = 'login'

    def get(self, request):
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        return render(request, self.template_name, context={'tickets': tickets, 'reviews': reviews})
