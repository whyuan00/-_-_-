<template>
  <div class="container">
    <h5 class="item">주식 종목명: {{ stockproduct.itmsNm }}</h5>
    <h5 class="item">상품 고유 번호: {{ stockproduct.isinCd }}</h5>
    <h5 class="item">주식 시장: {{ stockproduct.mrktCtg }}</h5>
    <hr class="divider">
  </div>
</template>

<script setup>

defineProps({
  stockproduct: Object
})
</script>

<style scoped>
.container {
text-align: left; 
}

.item {
margin-bottom: 5px; 
}

.divider {
border: none; 
border-bottom: 1px solid #ccc; 
margin: 10px 0; 
}
</style>