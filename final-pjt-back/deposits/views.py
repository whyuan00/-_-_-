from urllib import response
from django.shortcuts import render
import requests
import pprint
from django.conf import settings
import xml.etree.ElementTree as ET
from django.http import JsonResponse
from django.db.migrations import serializer
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, StockProductsSerializer, FundProductsSerializer, FavProductSerializer, FavSavingProductSerializer
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, StockProducts, FundProducts, FavProduct, FavSavingPrdt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import xmltodict 
from datetime import datetime
import json
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


# 0. '.env'에 있는 API_KEY 가져오기
api_key = settings.DEPOSITS_API_KEY
stock_api_key = settings.STOCK_API_KEY
fund_api_key = settings.FUND_API_KEY

# Create your views here.
# 0. check data structure

def index(request):

    # 0-1. 공공데이터 - 주식
    # url = f'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={stock_api_key}&numOfRows=2806&pageNo=1'
    # 0-2. 공공데이터 - 펀드
    url = f'http://apis.data.go.kr/1160100/service/GetFundProductInfoService/getStandardCodeInfo?serviceKey={fund_api_key}&numOfRows=20&pageNo=1'
    response = requests.get(url)

    # print(response.status_code)
    # print(response.content)

    # XML을 JSON으로 변환
    xml_data = response.content
    json_data = xmltodict.parse(xml_data)

    return JsonResponse(json_data, safe=False)

    # # 0-3. 금융감독원 - 정기예금 및 적금

    # url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'  
    # url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # response = requests.get(url).json()
    # return JsonResponse(response, safe=False)


### save data ### 
# 1. 정기예금 상품 목록 및 옵션 목록 저장
#    - 정기예금 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - 정기예금 상품에 따른 옵션 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - topFinGrpNo=020000 --> 금융회사가 속한 권역 코드: 은행 기준으로 추출

def save_deposit_products(request):
    
    # 1. API 가져오는 URL 작성
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 2. JOSN 형식으로 바꿔서 resoponse에 넣어줌
    response = requests.get(url).json()
    baseListresponse = response['result']['baseList']
    optionListresponse = response['result']['optionList']
    
    
    for li in baseListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_deposit_products = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        

        # 유효성 검증 및 저장 또는 업데이트
        try:
            product_instance = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            for key, value in save_deposit_products.items():
                setattr(product_instance, key, value)
            product_instance.save()

        except DepositProducts.DoesNotExist:
            serializer = DepositProductsSerializer(data=save_deposit_products)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
    for li in optionListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')
        
        save_deposit_products = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }

        for product in DepositProducts.objects.filter(fin_prdt_cd = save_deposit_products['fin_prdt_cd']):
            save_deposit_products['product'] = product.pk

            serializer = DepositOptionsSerializer(data=save_deposit_products)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
            break
                    
                    
    return JsonResponse({ 'message':'save-good!' })


### save data ### 
# 2. 적금 상품 목록 및 옵션 목록 저장
#    - 적금 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - 적금 상품에 따른 옵션 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - topFinGrpNo=020000 --> 금융회사가 속한 권역 코드: 은행 기준으로 추출

def save_saving_products(request):
    
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    baseListresponse = response['result']['baseList']
    optionListresponse = response['result']['optionList']
    
    # # 2-1. baseListresponse --> model 1.
    for li in baseListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        # 저장할 데이터 필드
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        
        
        # 유효성 검증 및 저장 또는 업데이트
        try:
            product_instance = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            for key, value in save_data.items():
                setattr(product_instance, key, value)
            product_instance.save()
        
        except SavingProducts.DoesNotExist:
            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    # 2-2. optionListresponse --> model 2.
    # OptionList에서는 null 값 존재, -1 값 부여
    
    for li in optionListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm', '')
        intr_rate = li.get('intr_rate', -1)
        intr_rate2 = li.get('intr_rate2', -1)
        save_trm = li.get('save_trm', -1)
        
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        
        for product in SavingProducts.objects.filter(fin_prdt_cd = save_data['fin_prdt_cd']):
            save_data['product'] = product.pk

            serializer = SavingOptionsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
            break

    return JsonResponse({ 'message':'save-good!' })

### check data ### 
# 3. 적금 상품 or 예금 상품 금리 순으로 보여주기 
#    - 적금 상품 목록을 받아와 우대 금리 순으로 정렬하고, top 5 상품 리스트 출력
#    - 예금 상품 목록을 받아와 우대 금리 순으로 정렬하고, top 5 상품 리스트 출력

### 3-0-1. 예금 상품 - 전체 for 예적금 상품 비교 page ! ###
#          - 해당 금리에 따른 기간 별 금리 출력을 위해, 출력 형식을 재구성 --> 다른 방법이 있을까 고민.....

@api_view(['GET'])
def deposits_all_product(request):
    if request.method == 'GET':
        max_rate_options = DepositOptions.objects.prefetch_related('product')
        
        response_data = []
        product_map = {}
        for option in max_rate_options:
            product_data = {
                'kor_co_nm': option.product.kor_co_nm,
                'fin_prdt_nm': option.product.fin_prdt_nm,
                'etc_note': option.product.etc_note,
                'join_deny': option.product.join_deny,
                'join_member': option.product.join_member,
                'join_way': option.product.join_way,
                'spcl_cnd': option.product.spcl_cnd
            }
            
            option_data = {
                'intr_rate_type_nm': option.intr_rate_type_nm,
                'intr_rate': option.intr_rate,
                'intr_rate2': option.intr_rate2,
                'save_trm': option.save_trm
            }
            
            product_cd = option.product.fin_prdt_cd
            if product_cd not in product_map:
                product_map[product_cd] = {
                    'product_data': product_data,
                    'options': []
                }
                
            product_map[product_cd]['options'].append(option_data)
        
        for product_cd, data in product_map.items():
            response_data.append({
                'fin_prdt_cd': product_cd,
                'product_data': data['product_data'],
                'options': data['options']
            })
        
        return Response(response_data)

### 3-0-1-1. 예금 상품 - 하나의 detail view 출력 ###

@api_view(['GET'])
def deposits_detail(request, fin_prdt_cd):
    try:
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    except DepositProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    options = DepositOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    
    response_data = {
        'fin_prdt_cd': product.fin_prdt_cd,
        'product_data': {
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'etc_note': product.etc_note,
            'join_deny': product.join_deny,
            'join_member': product.join_member,
            'join_way': product.join_way,
            'spcl_cnd': product.spcl_cnd
        },
        'options': [{
            'intr_rate_type_nm': option.intr_rate_type_nm,
            'intr_rate': option.intr_rate,
            'intr_rate2': option.intr_rate2,
            'save_trm': option.save_trm
        } for option in options]
    }
    
    return Response(response_data)

### 3-0-2. 적금 상품 - 전체 for 예적금 상품 비교 page ! ###
#          - 해당 금리에 따른 기간 별 금리 출력을 위해, 출력 형식을 재구성 --> 다른 방법이 있을까 고민.....

@api_view(['GET'])
def save_all_product(request):
    if request.method == 'GET':
        max_rate_options = SavingOptions.objects.prefetch_related('product')
        
        response_data = []
        product_map = {}
        for option in max_rate_options:
            product_data = {
                'kor_co_nm': option.product.kor_co_nm,
                'fin_prdt_nm': option.product.fin_prdt_nm,
                'etc_note': option.product.etc_note,
                'join_deny': option.product.join_deny,
                'join_member': option.product.join_member,
                'join_way': option.product.join_way,
                'spcl_cnd': option.product.spcl_cnd
            }
            
            option_data = {
                'intr_rate_type_nm': option.intr_rate_type_nm,
                'intr_rate': option.intr_rate,
                'intr_rate2': option.intr_rate2,
                'save_trm': option.save_trm
            }
            
            product_cd = option.product.fin_prdt_cd
            if product_cd not in product_map:
                product_map[product_cd] = {
                    'product_data': product_data,
                    'options': []
                }
                
            product_map[product_cd]['options'].append(option_data)
        
        for product_cd, data in product_map.items():
            response_data.append({
                'fin_prdt_cd': product_cd,
                'product_data': data['product_data'],
                'options': data['options']
            })
        
        return Response(response_data)
    
### 3-0-2-1. 적금 상품 - 하나의 detail view 출력 ###

@api_view(['GET'])
def save_detail(request, fin_prdt_cd):
    try:
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    except SavingProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    options = SavingOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    
    response_data = {
        'fin_prdt_cd': product.fin_prdt_cd,
        'product_data': {
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'etc_note': product.etc_note,
            'join_deny': product.join_deny,
            'join_member': product.join_member,
            'join_way': product.join_way,
            'spcl_cnd': product.spcl_cnd
        },
        'options': [{
            'intr_rate_type_nm': option.intr_rate_type_nm,
            'intr_rate': option.intr_rate,
            'intr_rate2': option.intr_rate2,
            'save_trm': option.save_trm
        } for option in options]
    }
    
    return Response(response_data)

# 3-1. 예금 상품 - top5
@api_view(['GET'])
def deposits_check_top_rate(request):
    if request.method == 'GET':
        max_rate_options = DepositOptions.objects.prefetch_related('product').order_by('-intr_rate2')
        option_serializers = [DepositOptionsSerializer(option) for option in max_rate_options]
        product_data_list = [DepositProductsSerializer(option.product).data for option in max_rate_options]
        
        response_data = []
        cnt = 0
        for option_serializer, product_data in zip(option_serializers, product_data_list):
            data = {
                **option_serializer.data,
                'product': product_data
            }
            # print(data['save_trm'])
            if data['save_trm'] == 12:
                cnt+=1
                response_data.append(data)
            if cnt >=5:
                return Response(response_data)
    
# 3-2. 적금 상품 - top 5
@api_view(['GET'])
def save_check_top_rate(request):
    if request.method == 'GET':
        max_rate_options = SavingOptions.objects.prefetch_related('product').order_by('-intr_rate2')[:5]
        option_serializers = [SavingOptionsSerializer(option) for option in max_rate_options]
        product_data_list = [SavingProductsSerializer(option.product).data for option in max_rate_options]
        
        response_data = []
        for option_serializer, product_data in zip(option_serializers, product_data_list):
            data = {
                **option_serializer.data,
                'product': product_data
            }
            response_data.append(data)
        
        return Response(response_data) 
    
### save data ###
# 4. 주식 상품 목록 저장
#    - 주식 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - 주식 상품에 따른 옵션 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - numOfRows: 2806, 일자: 20240516 기준으로 추출

def save_stock(request):
    url = f'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={stock_api_key}&numOfRows=2806&pageNo=1'
    response = requests.get(url)

    # XML을 JSON으로 변환
    xml_data = response.content
    json_data = xmltodict.parse(xml_data)

    stock_data = json_data['response']['body']['items']['item']

    for li in stock_data:
        isinCd = li.get('isinCd')        
        itmsNm = li.get('itmsNm')           
        mrktCtg = li.get('mrktCtg')        
        trqu = li.get('trqu')               
        trPrc = li.get('trPrc')            
        lstgStCnt = li.get('lstgStCnt')         
        basDt = li.get('basDt')
        basDt = datetime.strptime(basDt, "%Y%m%d").date()
        fltRt = li.get('fltRt')
        
        # 이미 존재하는 isinCd인지 확인
        if StockProducts.objects.filter(isinCd=isinCd).exists():
            continue  # 이미 존재하면 건너뜀

        # 저장할 데이터 필드
        save_data = {
            'isinCd':isinCd,
            'itmsNm':itmsNm,
            'mrktCtg':mrktCtg,
            'trqu':trqu,
            'trPrc':trPrc,
            'lstgStCnt':lstgStCnt,
            'basDt':basDt,
            'fltRt':fltRt
        }
        
        # 유효성 검증
        serializer = StockProductsSerializer(data=save_data)
    
        # 유효성 검사 후 save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message': 'Stock data saved successfully'})

### check data ### 
# 5. 주식 상품을 체결량 순(높은/낮은) 순으로 보여주기 
#    - 주식 상품 목록을 받아와 체결량 순으로 정렬하고, top 5 상품 리스트 출력
#    - 주식 상품 목록을 받아와 체결량 순으로 정렬하고, bottom 5 상품 리스트 출력

@api_view(['GET'])
def check_stock_top_rate(request):
    if request.method == 'GET':
        
        top_rate_stock_products = StockProducts.objects.order_by('-trqu')[:5]
        serializer = StockProductsSerializer(top_rate_stock_products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def check_stock_bottom_rate(request):
    if request.method == 'GET':
        
        top_rate_stock_products = StockProducts.objects.order_by('-fltRt')[:5]
        serializer = StockProductsSerializer(top_rate_stock_products, many=True)
        return Response(serializer.data)
    
### save data ###
# 6. 펀드 상품 목록 저장
#    - 펀드 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - 펀드 상품에 따른 옵션 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - numOfRows: 20, 일자: 20240516 기준으로 추출

def save_fund(request):
    url = f'http://apis.data.go.kr/1160100/service/GetFundProductInfoService/getStandardCodeInfo?serviceKey={fund_api_key}&numOfRows=20&pageNo=1'
    response = requests.get(url)

    # XML을 JSON으로 변환
    xml_data = response.content
    json_data = xmltodict.parse(xml_data)

    fund_data = json_data['response']['body']['items']['item']

    for li in fund_data:
        asoStdCd = li.get('asoStdCd')        
        fndNm = li.get('fndNm')           
        ctg = li.get('ctg')        
        fndTp = li.get('fndTp')      
        basDt = li.get('basDt')    
        basDt = datetime.strptime(basDt, "%Y%m%d").date()
        
        # 이미 존재하는 isinCd인지 확인
        if FundProducts.objects.filter(asoStdCd=asoStdCd).exists():
            continue  # 이미 존재하면 건너뜀

        # 저장할 데이터 필드
        save_data = {
            'asoStdCd':asoStdCd,
            'fndNm':fndNm,
            'ctg':ctg,
            'fndTp':fndTp,
            'basDt':basDt,
        }
        
        # 유효성 검증
        serializer = FundProductsSerializer(data=save_data)
    
        # 유효성 검사 후 save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    return JsonResponse({'message': 'Fund data saved successfully'})

### check data ### 
# 7. 펀드 상품을 랜덤하게 보여주기
#    - 펀드 5개의 상품을 랜덤하게 보여주기
#    - order_by()에 '?'를 부여함으로써, 랜덤성 부여

@api_view(['GET'])
def check_fund_randomly(request):
    if request.method == 'GET':
        
        random_fund_products = FundProducts.objects.order_by('?')[:5]
        serializer = FundProductsSerializer(random_fund_products, many=True)
        return Response(serializer.data)

### 관심 상품 기능 ###

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, fin_prdt_cd):
    # 상품을 가져옵니다. 
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    
    # 현재 사용자의 선호 상품 목록을 가져옵니다. 
    user = request.user
    fav_product, created = FavProduct.objects.get_or_create(user=user)
    
    if product in fav_product.product.all():
        # 이미 선호 상품에 있는 경우, 해당 상품을 제거합니다.
        fav_product.product.remove(product)
        message = '관심 상품에서 제거되었습니다.'
    else:
        # 선호 상품에 추가합니다.
        fav_product.product.add(product)
        message = '관심 상품에 추가되었습니다.'
    
    return Response({'message': message})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likesSaving(request, fin_prdt_cd):
    # 상품을 가져옵니다. 
    product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    
    # 현재 사용자의 선호 상품 목록을 가져옵니다. 
    user = request.user
    fav_product, created = FavSavingPrdt.objects.get_or_create(user=user)
    
    if product in fav_product.product.all():
        # 이미 선호 상품에 있는 경우, 해당 상품을 제거합니다.
        fav_product.product.remove(product)
        message = '관심 상품에서 제거되었습니다.'
    else:
        # 선호 상품에 추가합니다.
        fav_product.product.add(product)
        message = '관심 상품에 추가되었습니다.'
    
    return Response({'message': message})

### 관심 상품 프로필 페이지로 보내기 ###
@api_view(['GET'])
def get_likes_deposits(request):
    if request.method == 'GET':
        
        likes_deposits_products = FavProduct.objects
        serializer = FavProductSerializer(likes_deposits_products, many=True)
        return Response(serializer.data)

# @api_view(['GET'])
# def get_likes_saving(request):
#     if request.method == 'GET':
        
#         likes_saving_products = FavSavingPrdt.objects
#         serializer = FavSavingProductSerializer(likes_saving_products, many=True)
#         return Response(serializer.data)
    
@api_view(['GET'])
def get_likes_saving(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'error': 'User not authenticated'}, status=401)
    
    likes_saving_products = FavSavingPrdt.objects.filter(user=user)
    serializer = FavSavingProductSerializer(likes_saving_products, many=True)
    return Response(serializer.data)