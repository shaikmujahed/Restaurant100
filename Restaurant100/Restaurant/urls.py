from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='HomeViwe'),
    path('BookTable/',views.BookTable, name='BookTable'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.RegisterPage, name='RegisterPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    

]

