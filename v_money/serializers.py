from v_money.models import VMoney
from rest_framework import serializers
from django.db.models import Sum


class VMoneySerializer(serializers.ModelSerializer):

    # total_money = serializers.SerializerMethodField()

    # def get_total_money(self, obj):
    #     sumIn = VMoney.objects.aggregate(Sum('deposit')).get('deposit__sum') or 0
    #     sumOut = VMoney.objects.aggregate(Sum('expense')).get('expense__sum') or 0
    # #     # print(in_field+return_field-out_field-lost_field)
    #     qq = sumIn - sumOut
    # #     # print(qq)
    #     return qq

    class Meta:
        model = VMoney
        fields = ("id_v_money", "date", "deposit", "expense", "remark")

