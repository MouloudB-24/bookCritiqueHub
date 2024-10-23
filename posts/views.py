from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from posts.models import Ticket, Review
from . import forms


class PostsView(LoginRequiredMixin, View):
    template_name = 'posts/posts.html'
    login_url = 'login'

    def get(self, request):
        tickets = Ticket.objects.filter(uploader=request.user)
        reviews = Review.objects.filter(user=request.user)
        return render(request, self.template_name, context={'tickets': tickets, 'reviews': reviews})


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
            return redirect('posts')
        return render(request, self.template_name, context={'form': form})


class ReviewView(LoginRequiredMixin, View):
    template_name = 'posts/review.html'
    form_class = forms.ReviewForm

    def get(self, request, ticket_id):
        form = self.form_class()
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        return render(request, self.template_name, context={'form': form, 'ticket': ticket})

    def post(self, request, ticket_id):
        form = self.form_class(request.POST, request.FILES)
        ticket = get_object_or_404(Ticket, pk=ticket_id)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('posts')
        return render(request, self.template_name, context={'form': form, 'ticket': ticket})


class TicketReviewView(LoginRequiredMixin, View):
    template_name = 'posts/ticket_review.html'
    ticket_form = forms.TicketForm
    review_form = forms.ReviewForm

    def get(self, request):
        ticket_form = self.ticket_form()
        review_form = self.review_form()
        return render(request, self.template_name, context={'ticket_form': ticket_form, 'review_form': review_form})

    def post(self, request):
        ticket_form = self.ticket_form(request.POST)
        review_form = self.review_form(request.POST, request.FILES)
        if any([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('posts')
        return render(request, self.template_name, context={'ticket_form': ticket_form, 'review_form': review_form})

