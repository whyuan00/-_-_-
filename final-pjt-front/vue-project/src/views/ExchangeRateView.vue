<template>
<!-- {{result}} -->
<div>
    <h3 class="title">현재 환율 정보를 알아볼까요?</h3>
    <p class="fontstyle">* 엔화, 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    <hr>
</div>
<div style="margin-top:100px">
  <div class="container mt-5" >
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card p-4 shadow-sm">
          <h1 class="text-center mb-4">환율 계산기</h1>
          <div class="mb-3">
            <input
              type="number"
              v-model="amount"
              class="form-control"
              placeholder="금액을 입력하세요"
            />
          </div>
          <div class="mb-3">
            <select v-model="fromCurrency" class="form-select">
              <option v-for="currency in currencies" :value="currency.cur_unit" :key="currency.cur_unit">
                {{ currency.cur_nm }} ({{ currency.cur_unit }}) 에서
              </option>
            </select>
          </div>
          <div class="mb-3">
            <select v-model="toCurrency" class="form-select">
              <option v-for="currency in currencies" :value="currency.cur_unit" :key="currency.cur_unit">
                {{ currency.cur_nm }} ({{ currency.cur_unit }}) 로 
              </option>
            </select>
          </div>
          <div class="text-center mt-4">
            <h3>결과: {{ result }} <span v-if="toData"> {{ toData.cur_unit}} </span></h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</template>

<script setup>
import axios from "axios";
import { ref,watch } from "vue";
import exchangeRates from "../../../../final-pjt-back/exchange_rates.json";

const data = ref(exchangeRates); // 배열형태의 환율정보
const fromCurrency = ref(""); // 선택된 국가1
const toCurrency = ref(""); // 선택된 국가2
const amount = ref(null); // 환율 계산할 값
const result = ref(0); //계산된 결과 값
const now = ref(false)


// currencies에 deal_bas_r (매매기준환율), cur_unit(단위), cur_nm(통화 국가와 이름) 만 넣기
const currencies = data.value.map((currency) => ({
  deal_bas_r: currency.deal_bas_r,
  cur_unit: currency.cur_unit,
  cur_nm: currency.cur_nm,
}));

// 셋 중 하나라도 변화있으면 함수 호출
watch([fromCurrency, toCurrency, amount,result], () => {
  calculate();
});


const fromData = ref(null)
const toData = ref(null)
function calculate() {
  // data.value 에서 fromCurrency 데이터 찾기
  // data.value 에서 toCurrency 데이터찾기
  fromData.value = data.value.find(currency => currency.cur_unit === fromCurrency.value);
  toData.value = data.value.find(currency => currency.cur_unit === toCurrency.value);
  // from과 to가 모두 선택되었을때 result 계산
 if (fromData.value && toData.value) {
    const fromRate = parseFloat(fromData.value.deal_bas_r.replace(/,/g, ''));
    const toRate = parseFloat(toData.value.deal_bas_r.replace(/,/g, ''));
    result.value = (fromRate* (amount.value )/ toRate ).toFixed(2);
  }
  console.log(result.value)
}
  

// 실시간으로 데이터 받을 경우 코드
// axios({
//   method: "get",
//   url: "http://127.0.0.1:8000/exchange_rate/",
// })
//   .then((response) => {
//     data.value = response.data;
//     console.log('환율데이터 저장')
//   })
//   .catch((error) => {
//     console.log(error);
//     console.log("환율정보 불러오기 실패");
//   });

</script>


<style scoped>
.container {
  font-family: 'Noto Sans KR', sans-serif;
  max-width: 1000px; /* 가로 너비를 더 크게 조정 */
  margin: auto;
}

.fontstyle {
  font-family: 'Noto Sans KR', sans-serif;
}

.card {
  font-family: 'Noto Sans KR', sans-serif;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 그림자 효과 추가 */
}

.form-control,
.form-select {
  font-family: 'Noto Sans KR', sans-serif;
  height: 45px;
  border-radius: 10px;
  border: 1px solid #ccc; /* 테두리 추가 */
}

h1 {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  font-size: 2rem;
}

h3 {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  color: #007bff;
}

.text-center {
  font-family: 'Noto Sans KR', sans-serif;
  text-align: center;
}
.title {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 100px; /* Nav 바의 높이만큼 여백 추가 */
    font-size: 30px;
    font-weight: bold;
    color: #333;
}
</style>

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
