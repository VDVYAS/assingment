from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('singup',views.singup,name="singup"),
    path('userinfo',views.userinfo,name="userinfo"),
    path('adminpage',views.adminpage,name="adminpage"),
    path('handlelogout',views.handlelogout,name="logout")
]