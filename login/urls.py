from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_or_regist,name='login_or_regist'),
    path('index/', views.index,name='index'),
]