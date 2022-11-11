from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render


@login_required
def home(request):
    return render(request, "common/home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authenticate(username=username, password=password)
    return LoginView.as_view()(request)


def log_out(request):
    logout(request)
    return redirect('logged_out')


def logged_out(request):
    return render(request, 'common/logged_out.html', {})
