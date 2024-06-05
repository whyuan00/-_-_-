<template>
  <div>
    <h5 class="title">해당 상품은 현재 인기있는 주식 종목입니다.</h5>
    <div class="divider"></div>
    <StockRecommendListItem 
      v-for="stockproduct in store.stockproducts"
      :key="stockproduct.id"
      :stockproduct="stockproduct"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import StockRecommendListItem from '@/components/StockRecommendListItem.vue'

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
