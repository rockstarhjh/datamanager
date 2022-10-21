from django.db.models import Sum

from products.models import Products
# from products.serializers import ProductSerializer
from .models import Price
from rest_framework import serializers


# class ProductSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Products
#         fields = ["category", "p_name"]
#         # fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    # p_info = ProductSerializer(many=True, read_only=True)
    # # p_info = serializers.StringRelatedField(many=True, read_only=True)
    # # print(p_info)
    # # p_info = serializers.RelatedField(source='products.category', read_only=True)
    # print(p_info.p_name[0])
    # category = Products.category
    # category = p_info.category
    # p_info = serializers.SerializerMethodField()
    # p_name = serializers.SerializerMethodField()

    # def get_p_info(self, obj):
    #     # print(obj)
    #     query = Products.objects.filter(product=obj)
    #     serializer = ProductSerializer(query)
    #     return serializer.data
    #
    # def get_p_name(self, obj):
    #     # print(obj)
    #     # qq = Products.objects.filter(idproducts=obj).get('p_name')
    #     return 1
    price_rate = serializers.SerializerMethodField()

    def get_price_rate(self, obj):
        price_rate = 0
        if obj.sellprice is not None and obj.buyprice is not None:
            sp = obj.sellprice
            bp = obj.buyprice
            price_rate = sp/bp - 1
        # print(price_rate)
        return format(price_rate, ".2f")+"%"

    class Meta:
        model = Price
        # fields = ['idprice', 'product', 'p_info', 'buyprice', 'renew_bp_date', 'sellprice', 'renew_sp_date', 'remark']
        # fields = ['p_info']
        fields = '__all__'
        # read_only_fields = ["p_info", ]
        # depth = 1
        # // 외래키 매핑 어려움 depth 사용
