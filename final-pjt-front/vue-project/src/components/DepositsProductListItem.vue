<template>
  <tr>
    <td class="name_td">
      <router-link :to="{ name: 'depositsdetailview', params: { id: stock.fin_prdt_cd } }">
        {{ stock.product_data.fin_prdt_nm }}
      </router-link>
    </td> 
    <td>{{ stock.product_data.kor_co_nm }}</td>
    <td>{{ getRateForTerm(6) }}</td>
    <td>{{ getRateForTerm(12) }}</td>
    <td>{{ getRateForTerm(24) }}</td>
    <td>{{ getRateForTerm(36) }}</td>
  </tr>
</template>
  
<script setup>
import { defineProps, onMounted } from 'vue'
import { RouterLink } from 'vue-router' 

const props = defineProps({
  stock: {
    type: Object,
    required: true,
  }
})


// Save Term에 따른 intr_rate2 값
const getRateForTerm = (term) => {
  const option = props.stock.options.find(option => option.save_trm === term)
  return option ? option.intr_rate2 : '-'
}

</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

td {
  border: 1px solid #ddd;
  padding: 8px;
  overflow: hidden;
  text-overflow: ellipsis; 
  white-space: nowrap; 
}

.name_td {
  padding: 8px;
  border: 1px solid #ddd;
  text-decoration: underline; 
  cursor: pointer; 
}
</style>
