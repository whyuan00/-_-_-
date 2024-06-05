<template>
    <div class="container">
      <h5 class="item">펀드 종목명: {{ fundproduct.fndNm }}</h5>
      <h5 class="item">펀드 유형: {{ fundproduct.fndTp }}</h5>
      <h5 class="item">자산 운용: {{ fundproduct.ctg }}</h5>
      <hr class="divider">
    </div>
</template>
  
<script setup>
  
  defineProps({
    fundproduct: Object
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