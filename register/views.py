from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    pass
    return render(request, 'register/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:
            #这里可以填入一些验证
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'register/login.html', {'message': message})
            if user.password == password:
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'register/login.html', {'message': message})
        else:
            return render(request, 'register/login.html', {'message': message})
    return render(request, 'register/login.html')


def register(request):
    pass
    return render(request, 'register/register.html')


def logout(request):
    pass
    return redirect('/register/')

