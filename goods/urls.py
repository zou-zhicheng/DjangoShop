"""DjangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from django.views.static import serve
from DjangoShop.settings import MEDIA_ROOT
from goods.view_base import GoodsListView
from goods.view_base import GoodsListView2
from goods.views import GoodsListView


urlpatterns = [
    path('list_base/', GoodsListView.as_view(), name='goods_list_base'),
    path('list_base2/', GoodsListView2.as_view(), name='goods_list_base2'),
    path('list/', GoodsListView.as_view(), name='list')
]
