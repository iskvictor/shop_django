"""shopapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


app_name ="shop"

urlpatterns = [
    url(r'^$', views.ShopBookList.as_view(), name='index'),
    url(r'^category/(?P<slug>[\w-]+)$', views.BookList.as_view(), name='post'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetail.as_view(), name='detail'),
    url(r'^auth/register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^search/?$', views.ProfileSearchView.as_view(), name='search'),
    url(r'^', views.ShopBookList.as_view(), name='index'),

]
