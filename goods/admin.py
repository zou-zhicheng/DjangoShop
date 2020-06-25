# goods/adminx.py
from django.contrib import admin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from .models import IndexAd


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    #显示的列
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type", "parent_category", "add_time"]


# @admin.register(GoodsBrand)
# class GoodsBrandAdmin(admin.ModelAdmin):
#     list_display = ["category", "image", "name", "desc"]
#
#
# @admin.register(BannerGoods)
# class BannerGoodsAdmin(admin.ModelAdmin):
#     list_display = ["goods", "image", "index"]
#
#
# @admin.register(HotSearch)
# class HotSearchAdmin(admin.ModelAdmin):
#     list_display = ["keywords", "index", "add_time"]


@admin.register(IndexAd)
class IndexAdAdmin(admin.ModelAdmin):
    list_display = ["category", "goods"]
