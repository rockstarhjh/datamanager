from .models import Acount
from rest_framework import serializers


class AcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acount
        fields = '__all__'
