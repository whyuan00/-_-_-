<template>
  <div class="container">
    <h1>도전하는 게 좋은 그대 !</h1>
    <h2>그대의 성향에 맞는 금융 상품은? <span class="highlight">"주식"</span></h2>
    <div class="recommendation-list">
      <StockRecommendList />
    </div>
  </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import StockRecommendList from '@/components/StockRecommendList.vue'

const store = useCounterStore()

onMounted(() => {
  store.stockRecommend()
})

</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

.container {
  text-align: center;
  background-color: #f5f7fa; 
  padding: 40px 20px; 
  margin-top: 40px; 
  border-radius: 12px; 
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); 
  font-family: 'Noto Sans KR', sans-serif; 
}

h1, h2 {
  font-weight: bold;
  margin: 0; 
}

h1 {
  font-size: 26px; 
  color: #007aff; 
  margin-bottom: 10px; 
}

h2 {
  font-size: 22px;
  color: #1d1d1f;
  margin-bottom: 20px;
}

.recommendation-list {
  background-color: #ffffff;
  border-radius: 8px; 
  padding: 20px; 
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); 
}

.recommendation-list ul {
  list-style: none; 
  padding: 0; 
  margin: 0; 
}

.recommendation-list li {
  font-size: 18px; 
  color: #1d1d1f; 
  padding: 10px 0; 
  border-bottom: 1px solid #e5e5ea; 
}

.recommendation-list li:last-child {
  border-bottom: none; 
}

.highlight {
  color: #ff5c5c; 
  font-size: 35px;
}
</style>
