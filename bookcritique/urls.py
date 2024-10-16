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

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

import authentication.views
from flux.views import HomePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.LogoutPageView.as_view(), name='logout'),
    path('change-password/', authentication.views.PasswordChange.as_view(), name='password_change'),
    path('change-password-done/', authentication.views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('signup/', authentication.views.SignupPageView.as_view(), name='signup'),
    path('home/', HomePage.as_view(), name='home'),
]
