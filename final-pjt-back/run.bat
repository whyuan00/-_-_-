REM 가상환경 만들기 
call python -m venv venv 

REM 가상환경 활성화 (가상환경을 사용하는 경우)
call venv\Scripts\activate

REM pip install
call pip install -r requirements.txt

REM 마이그레이션 파일 생성
python manage.py makemigrations

REM 데이터베이스에 마이그레이션 적용
python manage.py migrate

REM 데이터 로드
python manage.py loaddata data/deposit_products_data.json data/deposit_options_data.json data/saving_products_data.json data/saving_options_data.json data/fund_data.json data/stock_data.json

REM 개발 서버 실행
python manage.py runserver