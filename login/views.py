from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from django.db import connection

# 访问首页，如果已经登陆，则进入首页，否则跳转到登陆页面
from login.models import Userlist

# 登陆页面
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # 获取用户POST到服务器的账号和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # 通过ORM的方式，获取数据库的用户密码
            password_db = Userlist.objects.get(username=username).password
            # 判断密码是否正确，正确的话，就跳转到首页
            if password == password_db:
                # 把用户的username加入会话中
                request.session['username'] = username
                return redirect(reverse('index'))
            else:
                print('账号或者密码错误！')
                return render(request, 'login.html')
        except:
            print('账号尚未注册！')
            return render(request,'login.html')


# 首页
def index(request):
    return render(request,'index.html')





