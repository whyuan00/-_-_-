<template>
  <h3 class="title">모의 투자 게임으로 나의 투자성향을 확인해볼까요? </h3>
  <p class="fontstyle">* 게임 방법을 잘 숙지하신 후 시작해주세요. 투자완료 버튼을 누르면 결과창이 뜹니다 !</p>
  <hr>
  <div style="margin-top:20px">
    <div class="container my-5">
      <div class="card p-4 shadow-sm">
        <div class="top">
          <div class="graph">
            <GChart :type="chartType" :data="chartData" :options="chartOptions" class="mb-4" />
            <h1 class="highlight inline">남은 시간: <span :style="{ color: countdownColor }"> {{ time }} </span></h1>
            <h1 class="fontstyle">현재 코인 가격: <span class="text-primary">{{ cost }}</span></h1>
          </div>
        </div>
        <div class="my-info">
          <h2>투자 정보</h2>
          <div style="display: flex;">
            <p style="font-size:1.5rem; margin-top:10x; font-weight: bold;">현재 순 이익: {{ profit }} <p> 투자 가능 자산: {{ (availableasset / 10000).toLocaleString() }} 만원  </p></p>
            <div class="col buttonbox text-center" style="display: flex; margin-top: 20px;">
              <button v-if="!isGameStarted" class="btn btn-primary mr-2 startbutton" @click="toggleGame()">게임 (재)시작</button>
              <button v-else class="btn btn-secondary mr-2 stopbutton" @click="toggleGame()">일시정지</button>
            </div>
          </div>
          <div class="coinbuttonbox ">
            <p v-show="buynum * cost > availableasset " class="text-danger">구매 가능한 개수가 아닙니다</p>
            <p><span class="text-primary"> {{ buynum }}개 {{ (buynum * cost).toLocaleString() }} 원 구매</span> | 현재 최대 <span style="color:brown">  {{ (availableasset/cost).toFixed(0)-1 }}</span> 개 구매 가능  </p>

            <div class="coinbutton d-flex mb-3">
              <input v-model="buynum" type="text" class="form-control coininput" @keyup.enter="buy(buynum)">
              <button class="btn btn-outline-primary ml-2" @click="buy(buynum)">매수</button>
            </div>

            <p v-show="sellnum > mycoin" class="text-danger"> 판매 가능한 개수가 아닙니다</p>
            <p><span class="text-primary"> {{ (sellnum * cost).toLocaleString() }} 원
                판매</span> | 가진 코인 개수: {{ mycoin }} 개 </p>

            <div class="coinbutton d-flex">
              <input v-model="sellnum" type="text" class="form-control coininput" @keyup.enter="sell(sellnum)">
              <button class="btn btn-outline-primary ml-2" @click="sell(sellnum)">매도</button>
            </div>


          </div>
        </div>
        <div class="row my-4">

        </div>
        <div class="row my-4 text-center">
          <p class="text-warning text-wrap" style="text-align:start"> ※ 투자 완료 시까지 판매하지 않은 코인은 D-day의 가격으로 자동
            환산됩니다 <br /> <span>※ 게임을 처음부터 다시 하려면 페이지를 새로 고침 해주세요</span></p>
          <button class="btn btn-success mx-auto" @click="complete">투자완료</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
// npm i vue-google-charts
import axios from 'axios'
import { ref, computed, watch } from 'vue'
import { GChart } from 'vue-google-charts';
import { type, data, options } from './GoogleChartData';
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const username = ref(null)
computed(() => {
  User.value = store.User
  username.value = store.User.username
})

const store = useCounterStore()
const router = useRouter()
const chartType = ref(type)
const chartData = ref([['date', '코인 가격']])
const chartOptions = ref(options)

// 코인 가격 & 현재 시간 저장  
const cost = ref(0)
const time = ref(null)

const totalasset = ref(null) // 총자산 -> 투자 완료시 보유한 코인까지 환산한 자산
const availableasset = ref(1000000) // 현재 투자가능한 자산
const profit = ref(0)
watch(availableasset, (newValue, oldValue) => {
  profit.value = newValue - 1000000;
});
const mycoin = ref(0) // 현재 가진 코인 개수
const buycount = ref(0) // 투자횟수
const beforecoinvalue = ref(0) // 직전에 산 코인 가격 

const value1 = ref(0) // 한번에 투자할떄의 금액이 현재 자산대비 몇%인지(투자 완료시 투자 횟수로 나눌것)
const value2 = ref(0) // 이전 투자시의 코인가격과 현재 투자시의 코인가격 비교(투자 완료시 투자 횟수-1로 나눌것)
const value3 = ref(0) // 최종 투자 총액이 시작 자신의 몇% 차지하는지 비교(투자 완료시 최종결정)

const isGameStarted = ref(false)

const toggleGame = () => {
  isGameStarted.value = !isGameStarted.value
  if (isGameStarted.value) {
    start()
  } else {
    stop()
  }
}




function setvalue1(res) { // 변수 1 계산하는 함수
  if (res < 0.1) {
    value1.value += 1
  } else if (res < 0.2) {
    value1.value += 2
  } else if (res < 0.3) {
    value1.value += 3
  } else if (res < 0.4) {
    value1.value += 4
  } else {
    value1.value += 5
  }
}
// 변수 2 계산하는 함수 -> beforecoinvalue의 이전값과 이후값비교
watch(beforecoinvalue, (newvalue, oldvalue) => {
  if (oldvalue != 0) {
    if (oldvalue * 0.95 < newvalue && newvalue < oldvalue * 1.05) {
      value2.value += 3
    } else if (oldvalue < newvalue) {
      value2.value += 1
    } else if (oldvalue > newvalue) {
      value2.value += 5
    }
  }
});


const buynum = ref(null)
const sellnum = ref(null)

// 투자시마다 바뀌어야하는 변수: availableasset, mycoin, buycount, beforecoinvalue

function buy(num) { // 코인 매수 
  if (!num) {
    alert('유효한 값을 입력하세요'); return
  }
  num = parseInt(num)
  const buycost = cost.value * num // 현재 투자하려는 가격
  if (buycost > availableasset.value || buycost <= 0) {
    alert('구매 가능한 금액이 아닙니다.'); return
  }
  else {
    availableasset.value -= buycost; mycoin.value += num; buycount.value += 1; beforecoinvalue.value = cost.value;
    setvalue1(buycost / availableasset.value) // 투자가능 금액 대비 한번 투자시의 금액 
    value3.value += buycost //투자금액 추가
    buynum.value = ''
  }
}
function sell(num) { //코인 매도
  if (!num) {
    alert('유효한 값을 입력하세요'); return
  }
  num = parseInt(num)
  if (num > mycoin.value || num <= 0) {
    alert('판매 가능한 개수가 아닙니다.'); return
  }
  else {
    availableasset.value += num * cost.value; mycoin.value -= num;
    sellnum.value = ''
  }
}
const level = ref(null)
// 투자 완료시 value1,2,3 결정하고 db저장, 수익profit db저장, 총자산 totalasset 저장, 투자횟수buycount 저장
const complete = function () { // 투자 완료
  // 확인 또는 취소를 선택할 수 있는 알림 대화 상자 표시
  if (confirm('정말 투자를 완료하실 건가요?')) {
    // '확인'을 선택한 경우 게임 페이지로 이동
    router.push({ name: 'gameview' });
    if (buycount.value === 0) {
      value1.value = 0
    } else { value1.value /= buycount.value }
    if (buycount.value > 1) {
      value2.value /= (buycount.value - 1)
    } else { value2.value = 0 }
    value3.value = (function () {
      // 최종 투자 총액이 시작 자신의 몇% 차지하는지 비교(투자 완료시 최종결정)
      const totalpercent = value3.value / 1000000
      if (totalpercent === 0) {
        return 0
      } else if (totalpercent <= 0.2) {
        return 1
      } else if (totalpercent <= 0.4) {
        return 2
      } else if (totalpercent <= 0.6) {
        return 3
      } else if (totalpercent <= 0.8) {
        return 4
      } else { return 5 }
    })()
    // 최종자산은 보유코인환산
    totalasset.value = availableasset.value + 596 * mycoin.value;
    // profit 을 총매출-초기자산(백만원)으로 정의해서 코인 판돈도 추가해야함
    profit.value += 596 * mycoin.value;
    // 최종 성향 결정
    level.value = (function () {
      // 최종 투자 총액이 시작 자신의 몇% 차지하는지 비교(투자 완료시 최종결정)
      const finalvalue = value1.value + value2.value + value3.value
      if (finalvalue < 3) {
        return 1
      } else if (finalvalue < 6) {
        return 2
      } else if (finalvalue < 9) {
        return 3
      } else if (finalvalue <= 12) {
        return 4
      } else { return 5 }
    })()

    axios({
      method: 'post',
      url: `${store.API_URL}/invest/${store.User.username}/`,
      data: {
        value1: value1.value.toFixed(2),
        value2: value2.value.toFixed(2),
        value3: value3.value.toFixed(2),
        lv: level.value,
        totalasset: totalasset.value,
        profit: profit.value,
        buycount: buycount.value,
      },
      headers: {
        Authorization: `Token ${store.Token}`
      }
    })
      .then((response) => {
        console.log('db저장완료')
        router.push({ name: 'checkresultview', params: { username: username }, query: { mydata: JSON.stringify(response.data) } });
        stop()
      })
      .catch((error) => {
        console.log(error)
        console.log('db저장실패')
        stop()
      })
  }
}
// '취소'를 선택한 경우 아무 작업도 수행하지 않음


let intervalid = null // clearinterval 을 위한 intervalid 변수 생성
function start() { // 1초에 한번씩 pushData 실행할 함수 start
  intervalid = setInterval(pushData, 400);
}
function stop() { // 일시정지
  console.log('멈춤')
  clearInterval(intervalid)
}

let i = 0; // 차트만드는 함수
const pushData = function () {
  //1. 화면에 보이는 데이터 개수 관리
  if (chartData.value.length > 30) {
    chartData.value.splice(1, 1)
  }
  //2. 데이터를 다 넣었으면 완료 페이지로
  if (i === data.length) {
    clearInterval(intervalid)
    console.log('투자완료')
    complete()
  }
  else {
    chartData.value.push(data[i])
    // 현재 시간& 코인 가격 표시
    cost.value = data[i][1]
    time.value = data[i][0]
    console.log(data[i][1])
  }
  i++;
}

// D-Day가 10일 남았을 때부터 색상을 변경
const countdownColor = ref('#007bff')
if (time.value !== null) {
  const match = time.value.match(/\d-/);
  if (match !== null) {
    daysLeft = parseInt(match[0]) // 문자열에서 숫자만 추출하여 정수로 변환
  } if (daysLeft <= 10) {
    countdownColor.value = 'red'
  }
}



</script>
<style scoped>
.startbutton {
  font-family: 'Noto Sans KR', sans-serif;
  width: 30%;
  height: 50px;
}

.stopbutton {
  font-family: 'Noto Sans KR', sans-serif;
  width: 30%;
  height: 50px;
}

.buttonbox {
  font-family: 'Noto Sans KR', sans-serif;
  justify-content: flex-end;
  align-items: center;
}

.container {
  font-family: 'Noto Sans KR', sans-serif;
  max-width: 800px;
  margin: auto;
}

.text-wrap {
  font-family: 'Noto Sans KR', sans-serif;
  overflow-wrap: break-word;
  /* 긴 단어를 줄바꿈하여 여러 줄로 나눔 */
  word-wrap: break-word;
  /* 오래된 브라우저 지원을 위한 속성 */
}

.card {
  font-family: 'Noto Sans KR', sans-serif;
  border-radius: 15px;
  width:1000px;
}

h1,
h2 {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
}

.text-warning {
  font-family: 'Noto Sans KR', sans-serif;
  color: #ffc107;
}

.text-primary {
  font-family: 'Noto Sans KR', sans-serif;
  color: #007bff;
}

.text-danger {
  font-family: 'Noto Sans KR', sans-serif;
  color: #dc3545;
}

.coininput {
  font-family: 'Noto Sans KR', sans-serif;
  height: 45px;
  border-radius: 10px;
}

.coinbutton {
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  align-items: center;
}

.coinbuttonbox p {
  margin-bottom: 5px;
  font-family: 'Noto Sans KR', sans-serif;
}

button {
  font-family: 'Noto Sans KR', sans-serif;
  border-radius: 10px;

}

.fontstyle {
  font-family: 'Noto Sans KR', sans-serif;
}

.btn-success {
  background-color: #007bff;
  /* 투자완료 버튼 배경색 변경 */
  border-color: #007bff;
  /* 투자완료 버튼 테두리 색상 변경 */
}
</style>