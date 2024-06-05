<template>
    <div class="content">
        <!-- <router-link to="/" class="btn btn-secondary mt-3">뒤로가기</router-link>/ -->
        <div>
            <!-- {{ user.id }} -->
            <h3 class="title">{{ user.username }}님이 관심있는 예적금 상품이에요 !</h3>
            <hr>
            <MyDepositsProducts :favProducts="favProducts"></MyDepositsProducts>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MyDepositsProducts from '@/components/MyDepositsProducts.vue';

const store = useCounterStore()
const favProducts = ref([]);
const API_URL = 'http://127.0.0.1:8000'

// 현재 사용자 정보 
const user = store.User

// 적금 관련
onMounted(async () => {
  try {
    const token = localStorage.getItem('token'); 
    const response = await axios.get(`${API_URL}/deposits/get-likes-deposits/`, {
      headers: {
        Authorization: `Token ${store.Token}`
      },
    });
    favProducts.value = response.data;
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

@media (max-width: 767px) {
    .form-group {
        margin-bottom: 20px;
    }
}
</style>
<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
