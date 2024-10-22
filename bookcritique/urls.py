"""
URL configuration for bookcritique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import authentication.views
import posts.views
import subscriptions.views
from flux.views import HomePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.LogoutPageView.as_view(), name='logout'),
    path('change-password/', authentication.views.PasswordChange.as_view(), name='password_change'),
    path('change-password-done/', authentication.views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('signup/', authentication.views.SignupPageView.as_view(), name='signup'),
    path('ticket/', posts.views.TicketView.as_view(), name='ticket'),
    path('ticket/<int:ticket_id>/review/', posts.views.ReviewView.as_view(), name='review'),
    path('ticket/review', posts.views.TicketReviewView.as_view(), name='ticket_review'),
    path('posts/', posts.views.PostsView.as_view(), name='posts'),
    path('subscriptions/', subscriptions.views.SubscriptionsView.as_view(), name='subscriptions'),
    path('follow/', subscriptions.views.FollowUserView.as_view(), name='following'),
    path('profile-photo/upload', authentication.views.UploadProfilePhoto.as_view(), name='upload_profile_photo'),
    path('home/', HomePage.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
