<template>
  <div>
    <h1>나의 투자 성향 확인하기</h1>
    <div v-if="mydata" class="investment-info">
      <p>
        나의 투자 성향은...
        <span style="color:blue; font-weight: bold; font-size:2rem" v-if="mydata.lv === 1">안정형!</span>
        <span style="color:blue; font-weight: bold; font-size:2rem" v-else-if="mydata.lv === 2">안정 추구형!</span>
        <span style="color:blue; font-weight: bold; font-size:2rem" v-else-if="mydata.lv === 3">위험 중립형!</span>
        <span style="color:blue; font-weight: bold; font-size:2rem" v-else-if="mydata.lv === 4">적극 투자형!</span>
        <span style="color:blue; font-weight: bold; font-size:2rem" v-else-if="mydata.lv === 5">공격 투자형!</span>
      </p>
      <div class="highlight">
        <p>나의 투자 수익 <span class="profit">{{ mydata.profit }} 원</span> | 투자 횟수 총 <span class="buycount">{{
          mydata.buycount }} 회</span></p>
      </div>
      <p>투자 결과 총 자산 {{ mydata.totalasset / 10000 }} (만)원</p>
      <div class="buttonbox" >
        <button @click="movetopage(mydata.lv)">나에게 딱 맞는 금융 상품을 추천 받고 싶다면? <span>click!</span></button>
      </div>
    </div>
    <div v-else>
      <p>저장된 데이터가 없습니다.</p>
    </div>
    <br />
    <div class="investment-info" v-if="score">
      <div class="rank-section">
        <h2>나의 등수는 ?</h2>
        <div class="rank-info">
          <p>
            현재 <span style="color:pink">  {{ score.total_invest }} </span> 개 기록 중
            <span class="user-rank"> {{ score.user_rank }} </span> 등!!
          </p>
        </div>
      </div>
      <div class="buttonbox" style="justify-content: space-around;">
        <button @click="movetopagecomunity"> 다른 사람 점수 보러가기 & 내 점수 자랑하러 가기 </button>
        <button class="custom-button small" @click="movetopagegame()"> 다시 게임 할래요 ! <span>click!</span> </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const mydata = ref(null);
const score = ref(null)

function movetopagegame() {
  if (confirm('정말 게임을 다시 할건가요?')) {
    router.push({ name: 'gameview' });
  }
}

onMounted(() => {
  mydata.value = JSON.parse(route.query.mydata);

  axios({
    method: 'get',
    url: `${store.API_URL}/invest/findout_latest_score/${mydata.value.user}/`
  })
    .then(response => {
      score.value = response.data
      console.log('내 최근 데이터 출력')
    })
    .catch(error => {
      console.log('내 최근 데이터출력 실패', error)
    })
    
    //store에 저장된 profit과 asset을 업데이트 
    store.getProfitData()
    store.getAssetData()
    console.log('정렬data업데이트')
});

function movetopage(pagenum) {
  if (pagenum === 1) {
    router.push({ name: 'lv1' });
  } else if (pagenum === 2) {
    router.push({ name: 'lv2' });
  } else if (pagenum === 3) {
    router.push({ name: 'lv3' });
  } else if (pagenum === 4) {
    router.push({ name: 'lv4' });
  } else {
    router.push({ name: 'lv5' });
  }
}

const movetopagecomunity = function () {
  router.push({ name: 'articleview' })
}
</script>

<style scoped>
h1 {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 500;
  color: #339af0;
  margin-bottom: 20px;
}

.investment-info {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  box-sizing: border-box;
  width: 700px;
  margin: auto;
}

p {
  font-size: 18px;
  margin: 10px;
}

.highlight {
  background-color: #fff3cd;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  padding: 10px;
}

.highlight p {
  margin: 0;
}

.highlight .profit,
.highlight .buycount {
  font-weight: bold;
  color: #dc3545;
}

.buttonbox {
  display: flex;
  gap: 12px;
  flex-direction: row;
  justify-content: flex-start;
  margin-top: 40px;
}

.buttonbox button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.buttonbox button:hover {
  background-color: #0056b3;
}

.buttonbox button span {
  font-weight: bold;
}

.rank-section {
  text-align: center;
}

.rank-section h2 {
  font-size: 1.8rem;
  color: #339af0;
  padding: 10px;
}

.rank-info {
  margin-top: 10px;
}

.rank-info p {
  font-size: 37px;
  margin: 0;
}

.user-rank {
  font-weight: bold;
  color: brown;
}
</style>
