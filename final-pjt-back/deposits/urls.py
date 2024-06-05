from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    path('deposits-all-product/', views.deposits_all_product, name='deposits_all_product'),
    path('deposits-all-product/<slug:fin_prdt_cd>/', views.deposits_detail, name='deposits_detail'),
    path('like-product/<slug:fin_prdt_cd>/', views.likes, name='like_product'),                         # 관심 정기예금 상품 등록
    path('like-saving-product/<slug:fin_prdt_cd>/', views.likesSaving, name='like_saving_product'),     # 관심 적금 상품 등록
    path('save-all-product/<slug:fin_prdt_cd>/', views.save_detail, name='save_detail'),
    path('save-all-product/', views.save_all_product, name='save_all_product'),
    path('deposits-check-top-rate/', views.deposits_check_top_rate, name='deposits_check_top_rate'),
    path('save-check-top-rate/', views.save_check_top_rate, name='save_check_top_rate'),
    path('save-stock/', views.save_stock, name='save_stock'),
    path('save-fund/', views.save_fund, name='save_fund'),
    path('check-stock-top-rate/', views.check_stock_top_rate, name='check_stock_top_rate'),
    path('check-stock-bottom-rate/', views.check_stock_bottom_rate, name='check_stock_bottom_rate'),
    path('check-fund-randomly/', views.check_fund_randomly, name='check_fund_randomly'),
    path('get-likes-deposits/', views.get_likes_deposits, name='get_likes_deposits'),
    path('get-likes-saving/', views.get_likes_saving, name='get_likes_saving'),
]