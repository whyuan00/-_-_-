from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
# Crdeate your views here.

# 입력받은 username 을 가진 user를 찾는 view함수
def userprofile(request,username):
    User = get_user_model()
    user = get_object_or_404(User, username = username)

    # json data 로 변환하기 위해 serializer 호출
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)