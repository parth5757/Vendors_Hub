from django.shortcuts import render
import re
from vadmin.models import *
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def signin(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(email=email, password=password)
    #     if user is not None:
    #         auth_login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Invalid login credentials.')
    #         return redirect('signin') 
    # return render(request, 'signin.html')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        sign = Sign
    return render(request, 'register.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return redirect('signup')
        user = User(email=email, password=password)
        user.save()
        return redirect('signin')
    else:
        return render(request, 'signup.html')
def error(request, undefined_route):
    return render(request, 'error_400.html')     