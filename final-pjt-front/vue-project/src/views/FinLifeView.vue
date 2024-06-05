<template>
    <div>
        <h3 class="title">예적금 상품을 알아볼까요?</h3>
        <RouterLink :to="{ name: 'depositsproductview'}">정기예금</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'saveproductview'}">정기적금</RouterLink>
        <hr>
    </div>
    <div>
        <RouterView/>  
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>


.title {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 100px; 
    font-size: 30px;
    font-weight: bold;
    color: #333;
}

</style>
<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
