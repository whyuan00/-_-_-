"""
Django settings for final_pjt_back project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 추가 import
import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR,'.env')
)

# 금융 API_KEY로 내 API 정리
DEPOSITS_API_KEY = env('API_KEY')

# 주식 API_KEY로 내 API 정리
STOCK_API_KEY = env('STOCK_API_KEY')

# 펀드 API_KEY로 내 API 정리
FUND_API_KEY = env('FUND_API_KEY')

# 환율 API_KEY로 내 API 정리
EXCHANGE_RATE_API_KEY = env('EXCHANGE_RATE_API_KEY')

# 지도 API_KEY로 내 API 정리
MAP_API_KEY=env('MAP_API_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5)ty8t*q5p5agwm9+^5=g$9sd-(_yuu*8ye8nrws&7%!6iwjk8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'comment',
    'map',
    'exchange_rate',
    'invest',
    'userprofile',
    'deposits',
    'accounts',

    # pip install djangorestframework 
    'rest_framework',
    'rest_framework.authtoken',


    # pip install dj-rest-auth
    'dj_rest_auth',
    

    # pip install 'dj-rest-auth[with_social]'
    # 'django.contrib.sites',
    # 'allauth.socialaccount',
    # pip install django-allauth
    'allauth',
    'allauth.account',


    # pip install django-cors-heㅇaders
    # cors 정책으로 인한 http요청 허용 
    'corsheaders',
    'django_extensions',

    # pip install django 
    'django.contrib.sites',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



]

# django social login 
SITE_ID = 1

REST_FRAMEWORK = {
    # Authentication: 모든 view함수가 토큰기반으로 인증하도록 설정 
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',

    ],
}

# 사용자 수정 
AUTH_USER_MODEL = 'accounts.User'

# 이메일 인증시스템 당장은 사용 x 
ACCOUNT_EMAIL_VERIFICATION = 'none'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
]

# 모든 도메인에 대해 CORS 허용
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

ROOT_URLCONF = 'final_pjt_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'final_pjt_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
