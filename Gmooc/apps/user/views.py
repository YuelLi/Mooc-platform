from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ResetPwdForm
from utils.email import send_email
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,"register.html",{"register_form": register_form})

    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            username=request.POST.get("email","")
            if UserProfile.objects.filter(email=username):
                return render(request,"register.html", {"msg":"The email address has been registered","register_form":register_form})
            password=request.POST.get("password","")
            user=UserProfile()
            user.username=username
            user.email=username
            user.password = make_password(password)
            user.is_active=False
            user.save()
            send_email(username,"r")
            return render(request,"login.html")
        else:
            return render(request,"register.html",{"register_form":register_form})


class LoginView(View):
    def get(self, request):
        return render(request,"login.html",{})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request,"login.html",{"msg":"User is not activated","login_form":login_form})
            else:
                return render(request,"login.html",{"msg": "Username or password you specified are incorrect", "login_form":login_form })
        else:
            return render(request, "login.html", {"login_form":login_form})


class ActivateView(View):
    def get(self,request,code):
        all_records= EmailVerifyRecord.objects.filter(code=code)
        if all_records:
            for record in all_records:
                email=record.email
                user = UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
            return render(request, "login.html")
        else:
            return render(request, "activate_fail.html")


class ForgotPwdView(View):
    def get(self,request):
        reset_form= ResetPwdForm()
        return render(request, "resetpwd.html",{"reset_form":reset_form})

    def post(self,request):
        reset_form= ResetPwdForm(request.POST)
        if reset_form.is_valid():
            email =request.POST.get("email","")
            send_email(email,"f")
            return render(request,"send_success.html")
        else:
            return render(request,"resetpwd.html",{"reset_form":reset_form})