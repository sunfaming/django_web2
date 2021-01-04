from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
"""
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import AnonymousUser

# Create your views here.

def index(request,):
    username = request.user
    return render(request,'Myapp/index.html',locals())
 
# 登录
def login(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        n = authenticate(username=username,password=password)
        if n:
            # 登陆成功即可获取当前登录用户，返回主页
            login(request,user=n)
            return redirect('/')
    # 失败重定向到登录页
    return render(request, 'users/login.html')
 
# 注册
def register(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        # 校验注册，名字不可重复
        u = User.objects.filter(username=username).first()
        if u:
            info = '该用户名已被注册'
            return render(request,'users/ERROR.html',{'info':info})
        else:
            # 注册成功，创建用户
            User.objects.create_user(
                username=username,
                password=password
            )
            # 重定向到登录页面
            return HttpResponseRedirect('/tologin/')
    # 注册失败，重新注册
    return render(request,'users/register.html')
 
def lagout(request):
    logout(request)
    return redirect('/')
"""

def register(request):
    # 注册新用户
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示空表单或指出表单无效
    context = {'form': form}
    return render(request, 'registration/register.html', context)