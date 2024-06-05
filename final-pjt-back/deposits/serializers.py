from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, StockProducts, FundProducts, FavProduct, FavSavingPrdt

# 정기예금 - 상품
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# 정기예금 - 상품옵션
class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=DepositProducts.objects.all())
    
    class Meta:
        model = DepositOptions
        fields = '__all__'

# 적금 - 상품
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

# 적금 - 상품옵션
class SavingOptionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=SavingProducts.objects.all())
    
    class Meta:
        model = SavingOptions
        fields = '__all__'
        
class StockProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProducts
        fields = '__all__'

class FundProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundProducts
        fields = '__all__'

# 관심상품 - 정기예금
class FavProductSerializer(serializers.ModelSerializer):
    product = DepositProductsSerializer(many=True, read_only=True)
    
    class Meta:
        model = FavProduct
        fields = '__all__'

# 관심상품 - 적금
class FavSavingProductSerializer(serializers.ModelSerializer):
    product = SavingProductsSerializer(many=True, read_only=True)
    
    class Meta:
        model = FavSavingPrdt
        fields = '__all__'