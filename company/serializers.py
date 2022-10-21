from .models import Company
from rest_framework import serializers


class ComSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
