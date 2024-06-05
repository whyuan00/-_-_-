from rest_framework import serializers
from .models import Invest
from django.contrib.auth import get_user_model


# 투자한 user의 정보 저장하고 불러올 시리얼라이저 
class InvestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Invest
        fields = '__all__'
        read_only_fields = ('user',)


User = get_user_model()
# 투자 정보 모두 불러올 시리얼라이저 
class InvestListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Invest
        fields = '__all__'
        read_only_fields = ('username',)
