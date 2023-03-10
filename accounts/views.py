from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.

User = get_user_model()


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('products:list'))
        return render(request, 'accounts/register.html')

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, 'Password didn\'t match')
            return redirect(reverse_lazy("accounts:register"))

        # check if the email exists
        exist = User.objects.filter(email=email).exists()

        if exist:
            messages.error(request, 'Email already exist.')
            return redirect(reverse_lazy("accounts:register"))

        user = User.objects.create_user(email=email, name=name, password=pass1)
        messages.success(request, "Account created successfuly.")
        return redirect(reverse_lazy("products:list"))


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('products:list'))
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, "Wrong Creadentials.")
            return redirect(reverse_lazy("accounts:login"))

        if user.is_blocked:
            messages.warning(request, "Your user is blocked.")
            return redirect(reverse_lazy("accounts:login"))

        login(request, user)

        messages.success(request, "You are logged in now.")
        return redirect(reverse_lazy("products:list"))


class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse_lazy("products:list"))
