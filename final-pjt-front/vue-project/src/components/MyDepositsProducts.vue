<template>
    <div>
      <div v-for="favProduct in favProducts" :key="favProduct.id">
          <div v-for="product in favProduct.product" :key="product.id">
              <div class="product-box-info">
                <router-link :to="{ name: 'mydepositsdetailView', params: { id: product.fin_prdt_cd } }">
                        <h4>{{ product.fin_prdt_nm }}</h4>
                </router-link>
                <p>{{ product.kor_co_nm }}</p>
            </div>
          </div>

      </div>
    </div>
    <div class="right-container">
    <MySavingProducts :favSavingProducts="favSavingProducts"></MySavingProducts>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, defineProps } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MySavingProducts from './MySavingProducts.vue';
import { RouterLink } from 'vue-router'

const favSavingProducts = ref([]);
const API_URL = 'http://127.0.0.1:8000'

// props로 받은 favProducts 선언
const props = defineProps({
favProducts: {
  type: Object,
  required: true,
}
})

const store = useCounterStore()

onMounted(async () => {
try {
  const token = localStorage.getItem('token'); 
  const response = await axios.get(`${API_URL}/deposits/get-likes-saving/`, {
    headers: {
      Authorization: `Token ${store.Token}`
    },
  });
  favSavingProducts.value = response.data;
} catch (error) {
  console.error('There was an error!', error);
};
});

</script>

<style scoped>
.title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 30px;
  font-weight: bold;
  color: #333;
}

.subtitle {
  color: #339af0 !important;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  margin-top: 50px;
  margin-bottom: 30px;
}

.product-box:hover {
box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
}

.product-box-info {
  font-family: 'Noto Sans KR', sans-serif;
  color: #333;
  margin: 10px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  transition: box-shadow 0.3s ease;
}
</style>
