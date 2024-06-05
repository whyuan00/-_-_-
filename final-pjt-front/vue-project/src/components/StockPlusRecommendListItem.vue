<template>
  <div class="container">
    <h5 class="item">주식 종목명: {{ stockplusproduct.itmsNm }}</h5>
    <h5 class="item">상품 고유 번호: {{ stockplusproduct.isinCd }}</h5>
    <h5 class="item">주식 시장: {{ stockplusproduct.mrktCtg }}</h5>
    <hr class="divider">
  </div>
</template>

<script setup>

defineProps({
  stockplusproduct: Object
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