from stocks.models import Stocks
from .models import Products
from rest_framework import serializers
from django.db.models import Sum


class ProductSerializer(serializers.ModelSerializer):
    # pstock = StocksSerializer(many=True, read_only=True)
    # pstock = p_id.aggregate(sum('pstock'))
    # print(pstock)
    total_stock = serializers.SerializerMethodField()
    office_stock = serializers.SerializerMethodField()
    warehouse_stock = serializers.SerializerMethodField()

    def get_total_stock(self, obj):
        # print(obj)
        in_field = Stocks.objects.filter(idproducts=obj).aggregate(Sum('in_field')).get('in_field__sum') or 0
        out_field = Stocks.objects.filter(idproducts=obj).aggregate(Sum('out_field')).get('out_field__sum') or 0
        return_field = Stocks.objects.filter(idproducts=obj).aggregate(Sum('return_field')).get('return_field__sum') or 0
        lost_field = Stocks.objects.filter(idproducts=obj).aggregate(Sum('lost_field')).get('lost_field__sum') or 0
        # print(in_field+return_field-out_field-lost_field)
        qq = in_field+return_field-out_field-lost_field
        # print(qq)
        return qq

    def get_office_stock(self,obj):
        in_field = Stocks.objects.filter(idproducts=obj, location="사무실").aggregate(Sum('in_field')).get('in_field__sum') or 0
        out_field = Stocks.objects.filter(idproducts=obj, location="사무실").aggregate(Sum('out_field')).get('out_field__sum') or 0
        return_field = Stocks.objects.filter(idproducts=obj,location="사무실").aggregate(Sum('return_field')).get(
            'return_field__sum') or 0
        lost_field = Stocks.objects.filter(idproducts=obj, location="사무실").aggregate(Sum('lost_field')).get('lost_field__sum') or 0
        qq = in_field + return_field - out_field - lost_field
        return qq

    def get_warehouse_stock(self,obj):
        in_field = Stocks.objects.filter(idproducts=obj, location="창고").aggregate(Sum('in_field')).get('in_field__sum') or 0
        out_field = Stocks.objects.filter(idproducts=obj, location="창고").aggregate(Sum('out_field')).get('out_field__sum') or 0
        return_field = Stocks.objects.filter(idproducts=obj, location="창고").aggregate(Sum('return_field')).get(
            'return_field__sum') or 0
        lost_field = Stocks.objects.filter(idproducts=obj, location="창고").aggregate(Sum('lost_field')).get('lost_field__sum') or 0
        qq = in_field + return_field - out_field - lost_field
        return qq

    class Meta:
        model = Products
        fields = ("idproducts", "category", "p_name", "office_stock", "warehouse_stock", "total_stock")

