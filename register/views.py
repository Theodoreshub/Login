from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    pass
    return render(request, 'register/index.html')


def login(request):
    pass
    return render(request, 'register/login.html')


def register(request):
    pass
    return render(request, 'register/register.html')


def logout(request):
    pass
    return redirect('/register/')

