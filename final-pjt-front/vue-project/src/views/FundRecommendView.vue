<template>
  <div class="container">
    <h1>안정적인 것을 추구하면서도 도전하고 싶은 그대 !</h1>
    <h2>그대의 성향에 맞는 금융 상품은? <span class="highlight">"펀드"</span></h2>
    <div class="recommendation-list">
      <FundRecommendList />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import FundRecommendList from '@/components/FundRecommendList.vue'

const store = useCounterStore()

onMounted(() => {
      store.fundRecommend()
})
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

.container {
  text-align: center;
  background-color: #f5f7fa; /* 연한 회색 배경 */
  padding: 40px 20px; /* 여백 추가 */
  margin-top: 40px; /* 위쪽 마진 추가 */
  border-radius: 12px; /* 둥근 테두리 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); /* 그림자 효과 */
  font-family: 'Noto Sans KR', sans-serif; /* 폰트 설정 */
}

h1, h2 {
  font-weight: bold; /* 글씨 굵게 */
  margin: 0; /* 마진 제거 */
}

h1 {
  font-size: 26px; /* 글씨 크기 */
  color: #007aff; /* 토스블루 색상 */
  margin-bottom: 10px; /* 아래 여백 */
}

h2 {
  font-size: 22px; /* 글씨 크기 */
  color: #1d1d1f; /* 진한 회색 */
  margin-bottom: 20px; /* 아래 여백 */
}

.recommendation-list {
  background-color: #ffffff; /* 흰색 배경 */
  border-radius: 8px; /* 둥근 테두리 */
  padding: 20px; /* 내부 여백 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); /* 그림자 효과 */
}

.recommendation-list ul {
  list-style: none; /* 리스트 스타일 제거 */
  padding: 0; /* 리스트 내부 여백 제거 */
  margin: 0; /* 리스트 외부 여백 제거 */
}

.recommendation-list li {
  font-size: 18px; /* 글씨 크기 */
  color: #1d1d1f; /* 진한 회색 */
  padding: 10px 0; /* 리스트 아이템 여백 */
  border-bottom: 1px solid #e5e5ea; /* 리스트 아이템 구분선 */
}

.recommendation-list li:last-child {
  border-bottom: none; /* 마지막 아이템 구분선 제거 */
}

.highlight {
  color: #ff5c5c; /* 주식에 해당하는 글자색 */
  font-size: 35px;
}
</style>
