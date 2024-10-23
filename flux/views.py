from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from posts.models import Ticket, Review
from subscriptions.models import UserFollows


class HomePage(LoginRequiredMixin, View):
    template_name = 'flux/home.html'
    login_url = 'login'

    def get(self, request):

        """following = UserFollows.objects.filter(user=request.user).value_list('followed_user', flat=True)
        followers = UserFollows.objects.filter(followed_user=request.user).value_list('user', flat=True)
        users = list(following) + list(followers) + [request.user.id]"""

        tickets = Ticket.objects.filter()
        reviews = Review.objects.filter()
        return render(request, self.template_name, context={'tickets': tickets, 'reviews': reviews})
