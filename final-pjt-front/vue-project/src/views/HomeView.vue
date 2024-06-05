<template>
  <v-app>
    <v-container class="d-flex justify-center align-center text-center">
      <div>
        <v-row class="letter-container">
          <v-col v-for="(char, index) in messageArray" :key="index" class="letter">
            <span :style="{ animationDelay: `${index * 0.1}s` }">{{ char === ' ' ? '\u00A0' : char }}</span>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </v-app>

</template>

<script setup>







import { ref, computed } from 'vue';
const message = ref('당신을 위한 금융상품, 지금 바로 여기에서 찾아보세요 !')
const messageArray = computed(() => message.value.split(''))
</script>

<style scoped>
.v-container {
  height: 100vh;
}

.letter-container {
  font-size: 2rem;
  font-weight: 500;
  color: #339af0; /* 토스 느낌의 연한 파란색 */
  font-family: 'Noto Sans KR', sans-serif;
}

.letter span {
  display: inline-block;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.5s forwards;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h1 {
    text-align: center;
}

.box {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%; /* 부모 요소의 너비의 90%를 차지합니다. */
    max-width: 600px; /* 최대 너비를 설정하여 너비가 너무 커지지 않도록 제한합니다. */
    margin: 0 auto; /* 가운데 정렬을 위해 왼쪽과 오른쪽 여백을 자동으로 설정합니다. */
    padding: 20px;
    border: 2px solid skyblue;
    border-radius: 10px;
    box-sizing: border-box;
}

</style>