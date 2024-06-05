from enum import unique
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

### 1-1. 정기 예금 상품 - 상품정보 DB
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)                              # 금융상품 코드 
    kor_co_nm = models.TextField()                                           # 금융회사 명
    fin_prdt_nm = models.TextField()                                         # 금융 상품명
    etc_note = models.TextField()                                            # 기타 유의사항
    join_deny  = models.IntegerField()                                       # 가입제한 (ex) 1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()                                         # 가입대상
    join_way = models.TextField()                                            # 가입 방법
    spcl_cnd = models.TextField()                                            # 우대조건
    
### 1-2. 정기 예금 상품 - 상품옵션 DB
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)   # 외래 키 관계 정의 필드(상품과 옵션 모델 -> 곧, 1:M (일대 다) 관계)
    fin_prdt_cd = models.TextField()                                         # 금융상품 코드 
    intr_rate_type_nm = models.CharField(max_length=100)                     # 저축 금리 유형명
    intr_rate = models.FloatField()                                          # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                                         # 최고 우대금리 [소수점 2자리]
    save_trm = models.IntegerField()                                         # 저축 기간 [단위: 개월]
    
### 2-1. 적금 상품 - 상품정보 DB
class SavingProducts(models.Model):                                          
    fin_prdt_cd = models.TextField(unique=True)                              # 금융상품 코드 
    kor_co_nm = models.TextField()                                           # 금융회사 명
    fin_prdt_nm = models.TextField()                                         # 금융 상품명
    etc_note = models.TextField()                                            # 기타 유의사항
    join_deny  = models.IntegerField()                                       # 가입제한 (ex) 1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()                                         # 가입대상
    join_way = models.TextField()                                            # 가입 방법
    spcl_cnd = models.TextField()                                            # 우대조건
    
### 2-2. 적금 상품 - 상품옵션 DB
class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)    # 외래 키 관계 정의 필드(상품과 옵션 모델 -> 곧, 1:M (일대 다) 관계)
    fin_prdt_cd = models.TextField()                                         # 금융상품 코드 
    intr_rate_type_nm = models.CharField(max_length=100)                     # 저축 금리 유형명
    intr_rate = models.FloatField()                                          # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                                         # 최고 우대금리 [소수점 2자리]
    save_trm = models.IntegerField()                                         # 저축 기간 [단위: 개월]


### 3. 주식 상품 - 상품 DB
class StockProducts(models.Model):
    isinCd = models.TextField(unique=True)                                   # ISIN 코드 (국제 채권 식별 번호,유가 증권(채권)의 국제인증 고유번호) 
    itmsNm = models.TextField()                                              # 종목명
    mrktCtg = models.TextField()                                             # 시장구분 (주식의 시장 구분(KOSPI, KOSDAQ, KONEX))
    trqu = models.IntegerField()                                             # 거래량 (체결수량의 누적합계)
    trPrc = models.IntegerField()                                            # 거래대금 (거래 건 별 체결가격*체결수량의 누적합계)
    lstgStCnt = models.IntegerField()                                        # 상장주식수 (종목의 상장주식 수)
    basDt = models.DateField()                                               # 기준일자
    fltRt = models.DecimalField(max_digits=5, decimal_places=2)              # 등락률

### 4. 펀드 상품 - 상품 DB
class FundProducts(models.Model):
    asoStdCd = models.TextField(unique=True)                                 # 협회포준코드
    fndNm = models.TextField()                                               # 편드명
    ctg = models.TextField()                                                 # 업권 구분 (자산운용)
    fndTp = models.TextField()                                               # 펀드유형 (재간접)
    basDt = models.DateField()                                               # 기준일자

### 관심 정기예금 상품 관련 - DB
class FavProduct(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ManyToManyField(DepositProducts, related_name='favorite_products')
    
    
### 관심 적금 상품 관련 - DB
class FavSavingPrdt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ManyToManyField(SavingProducts, related_name='favorite_products')
    
    