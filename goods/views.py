from goods.models import Goods
from goods.serializers import GoodsSerializer
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# class GoodsListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods,many=True)
#         return Response(goods_serialzer.data)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)


# class GoodsListView(generics.ListAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


# http://127.0.0.1:8000/goods/list/?page=2&page_size=80
# 结果显示
# HTTP 404 Not Found
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "detail": "无效页面。"
# }
# 原因是所有的数据条目加起来都没有80, 如果page_size=20就不会出错
class GoodsListView(generics.ListAPIView):
    '商品列表页'
    pagination_class = GoodsPagination    #分页
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

