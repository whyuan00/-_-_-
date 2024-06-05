from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from django.conf import settings
import requests
import os 


# 0. '.env'에 있는 API_KEY 가져오기
exchange_rate_api_key = settings.EXCHANGE_RATE_API_KEY

'''
# http요청 없이 백엔드 서버가 켜졌을때 바로 url에 들어가서 api 데이터 요청하는 함수  
# def update_exchange_rate_json(sender, **kwargs):
#     url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={exchange_rate_api_key}&data=AP01'
#     json_file_path = os.path.join(settings.BASE_DIR, 'exchange_rates.json')
    
#     response = requests.get(url)
#     data = response.json()

    # 폴더에 json형태로 저장
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
'''


@api_view(["GET"])
def exchange_rate(request):
    #한국 수출입은행 환율api 
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={exchange_rate_api_key}&data=AP01'
    json_file_path = 'exchange_rates.json'
    if os.path.exists(json_file_path):

        # JSON 파일이 이미 존재하는 경우 파일의 내용을 읽어서 반환
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

    else:
        response = requests.get(url)
        data = response.json()

        # JSON 파일이 존재하지 않는 경우 파일 저장하고 해당 파일 반환 
        with open('exchange_rates.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        

    return JsonResponse(data, safe=False)



