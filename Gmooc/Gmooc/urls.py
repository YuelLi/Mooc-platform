"""Gmooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import xadmin

from user.views import LoginView, RegisterView, ActivateView,ForgotPwdView,ResetPwdView, ModifyPwdView
from organization.views import InstructorListView, InstructorDetailView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('captcha/', include('captcha.urls')),
    path('activate/<code>/', ActivateView.as_view(), name="activate"),
    path('reset/',ForgotPwdView.as_view(),name="reset"),
    path('reset/password/<code>/',ResetPwdView.as_view(), name="reset_pwd"),
    path('modify/',ModifyPwdView.as_view(),name="modify_pwd" ),

    # organization urls
    path('org/', include('organization.urls')),

    # course urls
    path('course/',include('course.urls')),

    # instructor urls
    path('instr/', InstructorListView.as_view(),name="instr-list"),
    path('instr/detail/<instr_id>/', InstructorDetailView.as_view(),name="instr-detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
