from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from authentication.models import User
from .forms import FollowUserForm
from .models import UserFollows


class SubscriptionsView(LoginRequiredMixin, View):
    template_name = "subscriptions/subscriptions.html"

    def get(self, request):
        return render(request, self.template_name)


class FollowUserView(LoginRequiredMixin, View):
    template_name = "subscriptions/follow_user.html"
    form_class = FollowUserForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form": form, "user": request.user})

    def post(self, request):
        form = FollowUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            try:
                user_to_follow = User.objects.get(username=username)
                if user_to_follow == request.user:
                    messages.error(request, "Vous ne pouvez pas vous suivre vous-même!")
                elif UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                    messages.error(request, f"Vous suivez déjà {username}.")
                else:
                    UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
                    messages.success(request, f"Maintenant! Vous suivez {username}")

            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas !")
            return redirect("subscriptions")
        return render(request, self.template_name, context={"form": form})


class UnFollowUserView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        follow_relation = UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow)

        if follow_relation.exists():
            follow_relation.delete()
            messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")
        return redirect("subscriptions")
