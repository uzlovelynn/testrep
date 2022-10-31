"""more URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from. import views

urlpatterns = [
    path('', views.soft, name='soft'),
    path('BLOG/',views.blog_content.as_view(), name= "blog"),
    path('detail_view/<id>',views.detail_view, name= "detail_view"),
    path('blog_detail_view/<id>',views.blog_detail_view, name= "blog_detail_view"),
    # path('BLOG/', views.blog, name='blog'),
    path('ABOUT_US/', views.aboutus, name='aboutus'),
    path('FAQs/', views.faq, name='faqs'),
    path('REGISTRATION/', views.registration, name='registration'),
    path('LOGIN/', views.login, name='login'),
     # path('user_logout/',views.user_logout, name= "user_logout"),
    path('SEARCH/',views.searchview.as_view(), name= "search"),
]
