from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from django.db import connection

# 访问首页，如果已经登陆，则进入首页，否则跳转到登陆页面
from login.models import Userlist


def index(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = Userlist.objects.filter(username=username,password=password)
    print(user)
    # 把用户名存入到会话中
    request.session['username']=username
    print(request.session.items())
    if request.session['username']!=None:
        return render(request,'index.html')
    else:
        return render(request, 'login.html')
