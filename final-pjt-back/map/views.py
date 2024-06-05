from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import pandas as pd
import json 
from django.http import JsonResponse, HttpResponse
import os 

def get_map_api_key(request):
    MAP_API_KEY = settings.MAP_API_KEY
    return JsonResponse({'MAP_API_KEY': MAP_API_KEY})



def get_city_district_name(request):
    # 현재 파일이 있는 디렉토리의 경로
    current_directory = os.path.dirname(__file__)

    # 찾으려는 CSV 파일의 경로를 설정
    csv_file_path = os.path.join(current_directory, 'city_district.csv')
    
    # JSON 파일 경로 설정
    json_file_path = os.path.join(current_directory, 'city_district.json')
    
    df = pd.read_csv(csv_file_path)
    # print(df)
    
    grouped = df.groupby('시/도')['시/군/구'].apply(list).to_dict()
    
    # NaN 값을 공백으로 변경
    for k,v in grouped.items():
        # v = [NaN]
        for i, item in enumerate(v):
            if pd.isna(item):  # NaN 값인지 확인
                grouped[k][i] = ''


    # 딕셔너리를 JSON 형식으로 변환
    json_data = json.dumps(grouped, ensure_ascii=False, indent=4)


    # JSON 파일로 저장
    json_file_path = os.path.join(current_directory, 'city_district.json')
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(grouped, json_file, ensure_ascii=False, indent=4)

    return HttpResponse(json_data, content_type='application/json')