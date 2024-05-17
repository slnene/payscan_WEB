"""
URL configuration for payscan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from payscan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_login_status/', views.check_login_status, name='check_login_status'),
    path('check_user_type/', views.check_user_type, name='check_user_type'),
    path('',views.launch),
    path('login/', views.login_view, name='login'), #opens login form and proccesses it
    path('logout/', views.logout_view, name='logout'),
    path('afterlogin/', views.dashboard),   
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
 #   path('deposit/', views.deposit, name='deposit'),
 #  path('withdraw/', views.withdraw, name='withdraw'),
    path('payment/<int:business_id>/', views.payment, name='payment'),
    path('scanner/', views.scanner, name='scanner'),
    path('transaction_history/', views.transaction_history, name='transaction_history'),
    path('scanner/', views.scanner, name='scanner'),
    path('success/<int:transaction_id>/', views.payment_success, name='payment_success'),
    path('applaunch/',views.appLaunch),
        
    ##### Business suite ####
    path('register_business/', views.register_business, name='register_business'),
    path('login_business/', views.login_business, name='login_business'),
    path('afterlogin_business/', views.business_dashboard, name='afterlogin_business'),   
    path('payment_business/<int:business_id>/', views.business_payment, name='payment_business'),
    path('withdraw_business/', views.business_withdraw, name='withdraw_business'),


]
