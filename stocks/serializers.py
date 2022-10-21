from .models import Stocks
from rest_framework import serializers


class StocksSerializer(serializers.ModelSerializer):
    # pstock = serializers.SerializerMethodField()
    #
    # def get_pstock(self, obj):
    #     qq = obj.in_field + obj.return_field - obj.out_field - obj.lost_field
    #     # print(qq)
    #     return qq

    class Meta:
        model = Stocks
        fields = '__all__'
