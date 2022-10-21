from acount.models import Acount
from rest_framework import serializers

from datamanager.models import Notice


class AcountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acount
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
