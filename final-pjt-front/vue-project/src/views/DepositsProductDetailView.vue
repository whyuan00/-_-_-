<template>
    <div class="content" v-if="deposit">
        <h1 class="title">정기예금 상품의 세부 정보를 확인해보세요 !</h1>
        <RouterLink :to="{ name: 'depositsproductview'}">정기예금</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'saveproductview'}">정기적금</RouterLink>
        <hr>
        <div class="button-container">
            <button class="custom-button small" @click="appendproducts()" v-if="!isInterested">관심 금융상품에 추가할래요 !</button>
            <button class="custom-button small" @click="removeproducts()" v-else>관심 금융상품에서 제거할래요 !</button>
        </div>
        <div class="product-info">
            <h5 class="info-item"><strong>금융회사명:</strong> {{ deposit.product_data.kor_co_nm }}</h5>
            <h5 class="info-item"><strong>상품명:</strong> {{ deposit.product_data.fin_prdt_nm }}</h5>
            <h5 class="info-item"><strong>가입방법:</strong> {{ deposit.product_data.join_way }}</h5>
            <h5 class="info-item"><strong>우대조건:</strong> {{ deposit.product_data.spcl_cnd }}</h5>
            <h5 class="info-item"><strong>기타 유의사항:</strong></h5>
            <p v-html="formatEtcNoteText(deposit.product_data.etc_note)" class="etc-note"></p>
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
const deposit = ref(null)
const API_URL = 'http://127.0.0.1:8000'
const isInterested = ref(false);

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/deposits/deposits-all-product/${route.params.id}`
    })
    .then((res) => {
        deposit.value = res.data
    })
    .catch(err => console.log(err))
})

const formatEtcNoteText = (etcNote) => {
    if (!etcNote) return ''; // etcNote가 null이거나 정의되지 않은 경우 빈 문자열 반환
    return etcNote.replace(/\n/g, '<br>'); // 줄 바꿈을 <br> 태그로 치환하여 반환
}


function appendproducts() {
    console.log(store.Token)
    console.log(deposit)
    if (!confirm('관심 상품으로 등록하실건가요 ?')) {
        return;
    }
    
    const fin_prdt_cd = deposit.value.fin_prdt_cd;

    axios({
        method: 'post',
        url: `${API_URL}/deposits/like-product/${fin_prdt_cd}/`,
        headers: {
            Authorization: `Token ${store.Token}`
        }
    })
    .then(response => {
        // 성공적으로 추가되었을 때의 동작을 구현할 수 있음
        console.log(response.data.message);
        alert(response.data.message); // 성공 또는 실패 메시지 표시
        isInterested.value = true;
    })
    .catch(error => {
        // 오류 처리
        console.error('Error:', error);
        alert('관심 상품 추가에 실패했습니다.'); // 실패 시 메시지 표시
    });
}

function removeproducts() {
    if (!confirm('관심 상품을 제거하실건가요 ?')) {
        return;
    }
    
    const fin_prdt_cd = deposit.value.fin_prdt_cd;

    axios({
        method: 'post',
        url: `${API_URL}/deposits/like-product/${fin_prdt_cd}/`,
        headers: {
            Authorization: `Token ${store.Token}`
        }
    })
    .then(response => {
        // 성공적으로 제거되었을 때의 동작을 구현할 수 있음
        console.log(response.data.message);
        alert(response.data.message); // 성공 또는 실패 메시지 표시
        isInterested.value = false; // 관심 상품 여부를 false로 설정하여 버튼을 변경함
    })
    .catch(error => {
        // 오류 처리
        console.error('Error:', error);
        alert('관심 상품 제거에 실패했습니다.'); // 실패 시 메시지 표시
    });
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



</style>

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap"></link>