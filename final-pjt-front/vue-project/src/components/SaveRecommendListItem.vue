<template>
  <!-- {{ saveproduct }} -->
  <div class="container">
    <h5 class="item">적금 상품명: {{ saveproduct.product.fin_prdt_nm }}</h5>
    <h5 class="item">금융 회사명: {{ saveproduct.product.kor_co_nm }}</h5>
    <h5 class="item">저축 금리: {{ saveproduct.intr_rate }}</h5>
    <h5 class="item">최고 우대 금리: {{ saveproduct.intr_rate2 }}</h5>
    <h5 class="item">저축 기간: {{ saveproduct.save_trm }}개월</h5>
    <hr class="divider">
  </div>
</template>

<script setup>

defineProps({
  saveproduct: Object
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