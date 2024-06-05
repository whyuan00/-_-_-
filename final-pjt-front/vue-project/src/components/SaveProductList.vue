<template>
  <div>
    <div class="divider"></div>
    <h5>다음은 적금 상품입니다 !</h5>
    <p>단리의 경우, 우대 단리 기준으로 정보가 제공됩니다.</p>
    <table class="table">
      <thead>
        <tr>
          <th class="name_th" scope="col">적금 상품명</th>
          <th scope="col">금융 회사명</th>
          <th class="rate_th" scope="col">6개월</th>
          <th class="rate_th" scope="col">12개월</th>
          <th class="rate_th" scope="col">24개월</th>
          <th class="rate_th" scope="col">36개월</th>
        </tr>
      </thead>
      <tbody>
        <SaveProductListItem 
          v-for="stock in paginatedStocks"
          :key="stock.id"
          :stock="stock"
        />
      </tbody>
    </table>
    <div class="pagination">
      <button @click="prevPage" :disabled="page === 1">이전 페이지</button>
      <span>{{ `${page} /${Math.ceil(stocks.length / itemsPerPage)} 페이지 중` }}</span>
      <button @click="nextPage" :disabled="page * itemsPerPage >= stocks.length">다음 페이지</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import SaveProductListItem from '@/components/SaveProductListItem.vue'
import { defineProps } from 'vue'

const props = defineProps({
  stocks: {
    type: Array,
    required: true,
  }
})

const page = ref(1)
const itemsPerPage = ref(10)

const paginatedStocks = computed(() => {
  const start = (page.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return props.stocks.slice(start, end)
})

const nextPage = () => {
  if (page.value * itemsPerPage.value < props.stocks.length) {
    page.value++
  }
}

const prevPage = () => {
  if (page.value > 1) {
    page.value--
  }
}
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  table-layout: fixed; 
}

.table th, .table td {
  border: 1px solid #ddd;
  padding: 8px;
  overflow: hidden;
  text-overflow: ellipsis; 
  white-space: nowrap; 
}

.table th {
  background-color: #f2f2f2;
  font-weight: bold;
  text-align: center; 
}

.table td {
  text-align: left;
}

.pagination {
  display: flex;
  justify-content: space-between;
}

.pagination button {
  padding: 8px 16px;
  background-color: #339af0;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.name_th {
  padding: 8px;
  border: 1px solid #ddd;
  cursor: pointer; 
  width: 300px; 
}


.rate_th {
  padding: 8px;
  border: 1px solid #ddd;
  cursor: pointer; 
  width: 80px; 
}
</style>
