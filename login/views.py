from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.models import User   #导入django自带的user表


# 登陆或者注册
def login_or_regist(request):
    if request.method=='GET':
        return render(request, 'login/login_or_regist.html')
    else:
        if request.POST.get('regist'):
            print("正在进行用户注册")
            # 获取用户POST到服务器的账号和密码
            username = request.POST.get('user_name')
            password = request.POST.get('password')
            email = request.POST.get('user_email')
            try:
                # 把注册信息写入数据库中，返回的是注册的用户名，需要str()才能打印出来
                registAdd = User.objects.create_user(username=username, password=password, email=email,first_name=username,last_name=username,is_staff=0,is_active=1)
                if str(registAdd) == username:
                    print("注册成功")
                else:
                    print("注册失败")
                return render(request, 'login/login_or_regist.html')
            except:
                raise
                print('用户已经存在')
                return render(request, 'login/login_or_regist.html')
        else:
            print('正在进行用户登陆功能')
            # 获取用户POST到服务器的账号和密码
            username = request.POST.get('login_user_name')
            password = request.POST.get('login_password')
            # 正在验证用户名和密码
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                print('登陆成功，用户的username成功加入session中')
                return redirect(reverse('login_or_regist'))
            else:
                print('登陆失败')
                return render(request, 'login/login_or_regist.html')

def forgrt(request):
    return render(request,'login/forget.html')





