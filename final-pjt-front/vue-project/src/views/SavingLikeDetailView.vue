<template>
    <div class="content" v-if="save">
        <h1 class="title"><span class="highlight">{{ save.product_data.fin_prdt_nm }}</span>의 세부 정보를 확인해보세요 !</h1>
        <router-link to="/mypage" class="btn btn-secondary mt-3">뒤로가기</router-link>
        <div class="product-info">
            <button></button>
            <h5 class="info-item"><strong>금융회사명:</strong> {{ save.product_data.kor_co_nm }}</h5>
            <h5 class="info-item"><strong>상품명:</strong> {{ save.product_data.fin_prdt_nm }}</h5>
            <h5 class="info-item"><strong>가입방법:</strong> {{ save.product_data.join_way }}</h5>
            <h5 class="info-item"><strong>우대조건:</strong> {{ save.product_data.spcl_cnd }}</h5>
            <h5 class="info-item"><strong>기타 유의사항:</strong></h5>
            <p v-html="formatEtcNoteText(save.product_data.etc_note)" class="etc-note"></p>
        </div>
        <div>
            <RouterView/>  
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { RouterLink, RouterView } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const save = ref(null)
const API_URL = 'http://127.0.0.1:8000'
const isInterested = ref(false);

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/deposits/save-all-product/${route.params.id}`
    })
    .then((res) => {
        save.value = res.data
    })
    .catch(err => console.log(err))
})

const formatEtcNoteText = (etcNote) => {
    if (!etcNote) return '';
    return etcNote.replace(/\n/g, '<br>'); 
}

</script>

<style scoped>
.content {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 80px;
    padding: 20px;
    font-size: 18px; 
}

.title {
    text-align: left;
    margin-bottom: 20px;
    font-size: 30px;
    font-weight: bold;
    color: #333;
}

.product-info {
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 30px; 
}

.info-item {
    margin-bottom: 10px;
    font-size: 20px; 
    color: #555;
}

.etc-note {
    white-space: pre-line; 
    font-size: 18px; 
    color: #777;
}

.button-container {
    display: flex;
    justify-content: flex-end; 
    gap: 10px; 
    margin-top: 20px; 
}

.custom-button {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 400;
    background-color: #2196F3; 
    border: none;
    color: white;
    padding: 10px 20px; 
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px; 
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2); 
}

.small {
    padding: 8px 16px;
}
.highlight {
    color: #339af0 !important;
}
</style>

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap"></link>
