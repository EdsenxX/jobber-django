from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def landing_page(request):
    return render(request, 'LandingPage.html', {})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return redirect('home')
        else:
            messages.error(request, "Usuario y/o contraseña incorrectos")
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('login')

def sing_up(request):
    return render(request, 'singup.html', {})


@login_required(login_url="login")
def home(request):
    return render(request, 'Home.html', {
        'user': request.user
    })
