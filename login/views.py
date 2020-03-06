from django.shortcuts import render
from django.shortcuts import redirect
from . import models

# Create your views here.

def index(request):
    return render(request,'login/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写内容'
        if username.strip() and password:
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在'
                return render(request,'login/login.html',{'message':message})
            if user.password == password:
                print(username,password)
                return redirect('/index/')
            else:
                message = '密码不正确!'
                return render(request,'login/login.html',{'message':message})

        else:
            return render(request,'login/login.html',{'message':message})
    return render(request,'login/login.html')

def register(request):

    pass
    return render(request,'login/register.html')

def logout(request):

    pass
    return redirect("/login/")


