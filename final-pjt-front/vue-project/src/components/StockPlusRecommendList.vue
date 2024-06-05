<template>
  <div>
    <h5 class="title">해당 상품은 현재 인지도가 낮은 주식 종목입니다.</h5>
    <div class="divider"></div>
    <StockPlusRecommendListItem 
      v-for="stockplusproduct in store.stockplusproducts"
      :key="stockplusproduct.id"
      :stockplusproduct="stockplusproduct"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import StockPlusRecommendListItem from '@/components/StockPlusRecommendListItem.vue'

const store = useCounterStore()
</script>

<style scoped>
.title {
  margin-top: 0px;
  font-weight: bold; 
  text-shadow: 1px 1px 2px rgba(0,0,0,0.1); 
  margin-bottom: 20px;
}

.divider {
  border-bottom: 1px dashed #ccc; 
  margin-bottom: 10px; 
}
</style>
