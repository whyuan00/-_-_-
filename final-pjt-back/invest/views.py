from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import InvestListSerializer, InvestSerializer
from .models import Invest
from django.contrib.auth import get_user_model

from django.http import JsonResponse, HttpResponse
import json 
# 로그인 해야만 투자정보 생성/ 조회 가능
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated]) 
def invest(request, username):
    # username을 가진 사용자 user 가져오기
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        # invest table 에서 userid 가진 user 가져오기(외래키로 저장된 상태)
        user_invest = get_list_or_404(Invest, user=user.id)
        serializer = InvestSerializer(user_invest, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 굳이 필요없을듯? 
# 전체 투자 리스트 가져오는 뷰함수 
@api_view(['GET'])
# @permission_classes([IsAuthenticated]) 
def invest_list(request):
    if request.method == 'GET':
        InvestList = get_list_or_404(Invest)
        serializer = InvestListSerializer(InvestList, many=True)
        return Response(serializer.data)


# 1. 수익순, 2투자횟수 순으로 전체 데이터 정렬해서 출력하는 뷰함수.
@api_view(['GET'])
def profit_sorted_data(request):

    # 수익 순으로 전체 데이터 정렬
    sorted_data = Invest.objects.order_by('-profit','-buycount')
    serializer = InvestSerializer(sorted_data, many=True)
    
    return Response(serializer.data)

# 1. 총자산순, 2투자횟수 순으로 전체 데이터 정렬해서 출력하는 뷰함수.
@api_view(['GET'])
def asset_sorted_data(request):
    # 수익 순으로 전체 데이터 정렬
    sorted_data = Invest.objects.order_by('-totalasset', '-buycount')
    serializer = InvestSerializer(sorted_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def findout_latest_score(request, user_id):
    # 모든 투자 정보를 가져옵니다.
    InvestList = get_list_or_404(Invest)
    # 투자 정보를 직렬화합니다.
    serializer = InvestListSerializer(InvestList, many=True)
    
    # 해당 사용자의 가장 최근 투자 정보를 가져옵니다.
    user_data = Invest.objects.filter(user=user_id).order_by('-created_at').first()
    
    user_rank = None
    total_invest = Invest.objects.count()
    
    # 사용자 데이터가 존재할 경우에만 등수를 계산합니다.
    if user_data:
        # 해당 사용자의 수익보다 큰 수익을 가진 사용자의 수를 세고 1을 더하여 등수를 계산합니다.
        user_rank = Invest.objects.filter(profit__gt=user_data.profit).count() + 1
    
    # 응답으로 투자 정보, 총 사용자 수, 사용자 등수를 반환합니다.
    return Response({'data': serializer.data, 'total_invest': total_invest, 'user_rank': user_rank})