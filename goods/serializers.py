# goods/serializers.py
from goods.models import Goods
from goods.models import GoodsCategory
from rest_framework import serializers


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


# ModelSerializer实现商品列表页
# class GoodsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Goods
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
