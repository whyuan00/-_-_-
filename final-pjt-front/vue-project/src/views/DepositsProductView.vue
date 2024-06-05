<template>
  <div class="main-container">
    <div class="left-container">
      <h4>검색하기</h4>
      <h5>금융 회사명과 은행 상품명을 검색해보세요!</h5>
      <br>
      <span>금융 회사명: </span>
      <input type="text" v-model="searchCompany" placeholder="Search by company...">
      <br><br>
      <span>예금 상품명: </span>
      <input type="text" v-model="searchProduct" placeholder="Search by product name...">
      <br><br>
      <div>
        <span>예치 기간: </span>
        <label>
          <input type="checkbox" v-model="term6" @change="applyFilters"> 6개월
        </label>
        <label>
          <input type="checkbox" v-model="term12" @change="applyFilters"> 12개월
        </label>
        <label>
          <input type="checkbox" v-model="term24" @change="applyFilters"> 24개월
        </label>
        <label>
          <input type="checkbox" v-model="term36" @change="applyFilters"> 36개월
        </label>
      </div>
    </div>
    <div class="right-container">
      <DepositsProductList :stocks="filteredProducts" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DepositsProductList from '@/components/DepositsProductList.vue'

const searchCompany = ref('')
const searchProduct = ref('')
const store = useCounterStore()
const stocks = computed(() => store.stocks)

// 예치 기간 체크박스 상태
const term6 = ref(false)
const term12 = ref(false)
const term24 = ref(false)
const term36 = ref(false)

// 금융 회사 및 상품명으로 필터링
const filteredProducts = computed(() => {
  if (!searchCompany.value && !searchProduct.value && !term6.value && !term12.value && !term24.value && !term36.value) {
    return stocks.value
  }
  return stocks.value.filter(product => {
    const companyName = product.product_data.kor_co_nm.toLowerCase()
    const productName = product.product_data.fin_prdt_nm.toLowerCase()
    const searchCompanyTerm = searchCompany.value.toLowerCase()
    const searchProductTerm = searchProduct.value.toLowerCase()

    const matchesCompany = !searchCompany.value || companyName.includes(searchCompanyTerm)
    const matchesProduct = !searchProduct.value || productName.includes(searchProductTerm)

    // 예치 기간 필터링 추가
    const termMatches = (!term6.value || (product.options.some(option => option.save_trm === 6 && option.intr_rate2 !== '-'))) &&
                    (!term12.value || (product.options.some(option => option.save_trm === 12 && option.intr_rate2 !== '-'))) &&
                    (!term24.value || (product.options.some(option => option.save_trm === 24 && option.intr_rate2 !== '-'))) &&
                    (!term36.value || (product.options.some(option => option.save_trm === 36 && option.intr_rate2 !== '-')));

    return matchesCompany && matchesProduct && termMatches
  })
})

onMounted(() => {
  store.depositsAllproducts()
})
</script>

<style scoped>
.main-container {
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 20px;
}

.left-container {
  flex: 1;
  margin-right: 20px;
}

.right-container {
  flex: 2;
}

.content {
  margin-top: 80px;
}

/* 예치 기간 체크박스 스타일 */
.left-container label {
  margin-left: 10px; /* 세로로 배열하기 위해 블록 요소로 설정 */
}
</style>

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
