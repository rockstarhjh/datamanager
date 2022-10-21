"""datamanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from datamanager.views import Main, NoticeViewSet

router = DefaultRouter()

router.register('api', NoticeViewSet)

Main = Main.as_view({
    'get': 'list',
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main, name="home"),
    path('', include(router.urls), name='notice'),
    path('user/', include('user.urls')),
    path('company/', include('company.urls')),
    path('acount/', include('acount.urls')),
    path('stocks/', include('stocks.urls')),
    path('products/', include('products.urls')),
    path('v_money/', include('v_money.urls')),
    path('price/', include('price.urls')),
    path('chart/', include('chart.urls')),
    path('main/', Main, name='main'),
    # path('user/', include('django.contrib.auth.urls')),
]
