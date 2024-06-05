# serializers.py
from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model

# 커멘트 리스트 불러오는 시리얼라이저 
class CommentListSerializer(serializers.ModelSerializer):
    # readonly field??
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

# 커멘트 정보 생성하고 불러오는 시리얼라이저 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['user', 'created_at']