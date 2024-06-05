<template>
  <div style="margin: 23px; font-family: 'Noto Sans KR', sans-serif;">
    <h2 class="fontstyle" style="padding: 30px; margin: 10px; background-color: #f8f9fa; border-radius: 10px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); font-family: 'Noto Sans KR', sans-serif;">
      현재 수익 순위 1등은... <br />
      <span style="color:blue">{{ bestuser }} </span>님, <span style="color:brown">{{ (bestprofit/10000).toFixed(1) }}</span>(만)원 입니다!!
    </h2>
    <p>※ 순위는 최대 20등 까지만 보입니다. <br/>
    ※ 내 결과: <span style="background-color: rgb(224, 255, 255); padding: 2px;">&nbsp;&nbsp;&nbsp;</span> Light Cyan</p>
    <div class="scroll-container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">순위</th>
            <th scope="col">이름</th>
            <th scope="col">수익(만)</th>
            <th scope="col">투자 횟수</th>
            <th scope="col">총 자산(만)</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(data, index) in profitData.slice(0, 20)"
            :key="data.id"
            class="data">
            <th :style="{ backgroundColor: sameUser(data.user) ? 'rgb(224, 255, 255)' : 'inherit' }" scope="row">{{ index + 1 }} 위</th>
            <td :style="{ backgroundColor: sameUser(data.user) ? 'rgb(224, 255, 255)' : 'inherit' }">{{ data.username }}</td>
            <td :style="{ backgroundColor: sameUser(data.user) ? 'rgb(224, 255, 255)' : 'inherit' }">{{ (data.profit / 10000).toFixed(1) }} 원</td>
            <td :style="{ backgroundColor: sameUser(data.user) ? 'rgb(224, 255, 255)' : 'inherit' }">{{ data.buycount }} 번</td>
            <td :style="{ backgroundColor: sameUser(data.user) ? 'rgb(224, 255, 255)' : 'inherit' }">{{ (data.totalasset / 10000).toFixed(1) }} 원</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="buttonbox">
      <button class="custom-button small" @click="movetopagegame()">
        다시 게임 할래요 ! <span>click!</span>
      </button>
      </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const router = useRouter()
const store = useCounterStore();
const profitData = ref([]);
const bestuser = ref(null);
const bestprofit = ref(null);
const user = store.User; // 현재 사용자 이름

const sameUser = (userid) => {
  return userid === user.id;
};

watchEffect(() => {
  profitData.value = store.profitData;
  bestuser.value = profitData.value[0]?.username || null;
  bestprofit.value = profitData.value[0]?.profit || null;
});
function movetopagegame() {
  if (confirm('정말 게임을 다시 할건가요?')) {
    router.push({ name: 'gameview' });
  }
}

</script>

<style scoped>
.scroll-container {
  max-height: 400px; /* 원하는 높이로 조절 */
  overflow-y: auto;
}

h2 {
  margin: 40px;
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
</style>
