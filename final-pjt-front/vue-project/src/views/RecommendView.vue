<template>
    <div>
        <h3 class="title">오늘의 금융 유형 별 추천 상품을 알아볼까요?</h3>
        <p class="fontstyle">* 각 금융 상품의 특징을 고려한 것으로, 자신의 투자 성향을 확인하고 상품에 대해 알아보시는 것을 추천드립니다.</p>
        <hr>
    </div>
    <nav class="nav">
        <RouterLink class="nav-link " href="#" :to="{ name: 'stockplusrecommendview'}" > 도전주식추천 </RouterLink>
        <span class="nav-link">|</span>
        <RouterLink class="nav-link " href="#" :to="{ name: 'stockrecommendview'}" > 인기주식추천 </RouterLink>
        <span class="nav-link">|</span>
        <RouterLink class="nav-link " href="#" :to="{ name: 'fundrecommendview'}" > 펀드종목추천 </RouterLink>
        <span class="nav-link">|</span>
        <RouterLink class="nav-link " href="#" :to="{ name: 'saverecommendview'}" > 적금상품추천 </RouterLink>
        <span class="nav-link">|</span>
        <RouterLink class="nav-link " href="#" :to="{ name: 'depositsrecommendview'}" > 정기예금추천 </RouterLink>
    </nav>
        <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.product-box-info {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: bold;
    font-size: 30px;
    font-family: 'Noto Sans KR', sans-serif;
    color: #333;
    margin: 10px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    transition: box-shadow 0.3s ease;
}
.container {
    font-family: 'Noto Sans KR', sans-serif;
    color:deepskyblue;
    font-family: 'Roboto', sans-serif; 
    font-size: 50px; 
    font-weight: 600; 
    text-align: center; 
}

nav {
    font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
}

.title {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 100px; 
    font-size: 30px;
    font-weight: bold;
    color: #333;
}

.fontstyle {
    font-family: 'Noto Sans KR', sans-serif;
}
</style>
<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
