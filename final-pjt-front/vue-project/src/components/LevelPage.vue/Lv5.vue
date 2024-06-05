<template>
    <div>
        <h3 class="content"><span>공격 투자형</span>에게 추천하는 금융상품</h3>
        <div class="button-container">
            <button class="custom-button small" @click="movetopagerecommend()"> 다른 추천 상품도 구경할래요 ! <span>click!</span> </button>
        </div>
        <StockPlusRecommendView />
    </div>
</template>

<script setup>
import StockPlusRecommendView from '@/views/StockPlusRecommendView.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function movetopagerecommend() {
    router.push({ name: 'recommendview' });
    alert('상품 추천 페이지로 가볼까요?');
}
</script>

<style scoped>
.content {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 80px; 
    font-weight: 400;
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

.custom-button:hover {
    background-color: #0b7dda; 
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 400;
}

.small {
    padding: 8px 16px; 
}


.stock-item {
    font-size: 12px; 
    padding: 8px;
}

</style>

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
