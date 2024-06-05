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
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposits/', include('deposits.urls')),

    # 새로추가한 장고 rest_auth가 제공하는 앱으로 사용 
    path('accounts/', include('dj_rest_auth.urls')),
    # 등록기능 추가설정 -> 패키지 추가설치, app등록, url등록, migrate 
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),

    # username 의 프로필 페이지 url 
    path('userprofile/<username>/', include('userprofile.urls')),
    
    # invest정보 url
    path('invest/', include('invest.urls')),

    # 환율정보 받을 url
    path('exchange_rate/', include('exchange_rate.urls')),

    # 지도 api key 보낼 url
    path('map/api_key/', include('map.urls')),

    # 게시글로 보낼 url
    path('comment/',include('comment.urls')),
]
