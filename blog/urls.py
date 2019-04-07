from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('index/', views.index,name='index'),
    # path('article_page/Notice/<article_id>/', views.Notice,name='Notice'),
    # path('article_page/ranking/<article_id>/', views.ranking,name='ranking'),
    path('article_page/artical_detail/<Artical_pk>/', views.Artical_detail,name='artical_detail'),
]