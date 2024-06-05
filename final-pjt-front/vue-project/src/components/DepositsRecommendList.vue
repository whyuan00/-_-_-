<template>
  <div>
    <h5 class="title">해당 상품은 금리가 높은 예금 상품입니다.</h5>
    <div class="divider"></div>
    <DepositsRecommendListItem
      v-for="depositsproduct in store.depositsproducts"
      :key="depositsproduct.id"
      :depositsproduct="depositsproduct"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import DepositsRecommendListItem from '@/components/DepositsRecommendListItem.vue' 

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
