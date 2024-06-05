"""
URL configuration for final_pjt_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('findout_latest_score/<int:user_id>/',views.findout_latest_score),
    path('profit_sorted_data/', views.profit_sorted_data), # 수익 순으로 정렬 
    path('asset_sorted_data/', views.asset_sorted_data), # 자산 순으로 정렬 

    path('',views.invest_list), # 투자리스트 보여주는 url
    path('<str:username>/',views.invest), # 투자자의 정보 get/post url
    

]
