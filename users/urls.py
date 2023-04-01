from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('registerClient/', views.RegisterClient, name='registerClient'),
    path('registerShop/', views.RegisterShop, name='registerShop'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
