"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Content.views import (
    home_view,
    doc_view,
)

from Account.views import (
    register_view,
    login_view,
    account_view,
    logout_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Content
    path('', home_view, name="home"),
    path('documentation/', doc_view, name="doc"),

    # Account
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('logout/', logout_view, name="logout"),

    # Password-rest
     path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html',
             success_url='done'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html',
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # Password-change
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='password-change/password_change_done.html'
         ),
        name='password_change_done'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='password-change/password_change.html'
         ),
        name='password_change'),
]
