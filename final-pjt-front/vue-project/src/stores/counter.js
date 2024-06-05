import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()

  // 예적금 상품 알아보기 page !
  // stock --> 곧, 하나의 금융 상품이라고 생각하면 쉬움
  const stocks = ref([])

  // 추천 관련 변수 5가지
  const saveproducts = ref([])
  const depositsproducts = ref([])
  const fundproducts = ref([])
  const stockproducts = ref([])
  const stockplusproducts = ref([])

  // 회원가입
  const API_URL = 'http://127.0.0.1:8000'
  const User = ref(null)
  const Token = ref(null)
  const isLogin = ref(false)

  // profit과 asset 기준 정렬 데이터
  const profitData = ref(null)
  const assetData = ref(null)

  // 전체 comment 넣기 
  const CommentList= ref([
    {id:1,content:'hellow1'},
    {id:2,content:'hellow2'},
  ])

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        console.log('회원가입완료')
        const password = password1
        logIn({ username, password })
      })
      .catch(error => {
        console.log(error)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(response => {
        // 응답받은 토큰 저장 
        Token.value = response.data.key
        isLogin.value = true
        console.log('로그인 성공')
        // 홈으로 이동
        router.push({ name: 'home' })

        // 로그인 성공 후 사용자 정보 가져오기
        getUser(username)
          .then((response) => {
            User.value = response
            console.log(`${User.value.username}정보확인`)
          })
          .catch((error) => {
            console.log(error, '로그인 후 사용자 정보 갖고오기 실패')
          })
      })
      .catch(error => {
        console.log('로그인 실패', error)
      })
  }


  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${Token.value}`
      }
    })
      .then(response => {
        // 사용자 정보 삭제
        User.value = null
        // 사용자 토큰 삭제 
        Token.value = null
        isLogin.value = false
        console.log('로그아웃 성공');

        // 로컬 스토리지에서 Pinia 데이터 제거
        localStorage.removeItem('pinia-user');
        console.log('로컬 스토리지에서 유저 데이터 제거')

        
        // 홈으로 이동
        router.push({ name: 'home' })

      })
      .catch(error => {
        console.log('로그아웃 실패:', error);
      });
  };

  // response 값을 얻기위한 비동기(async & await)처리
  const getUser = async function (username) {
    const response = await axios.get(`${API_URL}/userprofile/${username}`);
    return response.data;
  }

  const stockRecommend = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/check-stock-top-rate/`
    })
      .then(response => {
        console.log('stockrecommend')
        stockproducts.value = response.data
      })
      .catch(error => {
        console.log('주식 상품추천 실패:', error)
      })
  };

  const stockplusRecommend = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/check-stock-bottom-rate/`
    })
      .then(response => {
        console.log('stockplusrecommend')
        stockplusproducts.value = response.data
      })
      .catch(error => {
        console.log('주식 상품추천 실패:', error)
      })
  };

  const fundRecommend = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/check-fund-randomly/`
    })
      .then(response => {
        console.log('fundrecommend')
        fundproducts.value = response.data
      })
      .catch(error => {
        console.log('펀드 상품추천 실패:', error)
      })
  };

  const saveRecommend = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/save-check-top-rate/`
    })
      .then(response => {
        console.log('saverecommend')
        saveproducts.value = response.data
      })
      .catch(error => {
        console.log('적금 상품추천 실패:', error)
      })
  };

  const depositsRecommend = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposits-check-top-rate/`
    })
      .then(response => {
        console.log('despositsrecommend')
        depositsproducts.value = response.data
      })
      .catch(error => {
        console.log('정기예금 상품추천 실패:', error)
      })
  };

  function depositsAllproducts() {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposits-all-product/`
    })
      .then(response => {
        stocks.value = response.data
      })
      .catch(error => {
        console.log('예금 상품 출력 실패:', error)
      })
  };

  function savingAllproducts() {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/save-all-product/`
    })
      .then(response => {
        stocks.value = response.data
      })
      .catch(error => {
        console.log('적금 상품 출력 실패:', error)
      })
  };


  const getProfitData = function(){
    axios({
      method: 'get',
      url: `${API_URL}/invest/profit_sorted_data/`
    })
      .then(response => {
        profitData.value = response.data
        console.log('profit데이터 호출')
      })
      .catch(error => {
        console.log('profit데이터 불러오기 실패:', error)
      })
  }
  const getAssetData = function(){
    axios({
      method: 'get',
      url: `${API_URL}/invest/asset_sorted_data/`
    })
      .then(response => {
        console.log('asset데이터 호출')
        assetData.value = response.data
      })
      .catch(error => {
        console.log('profit데이터 불러오기 실패:', error)
      })
    }

      const getCommentList = function(){
        axios({
          method: 'get',
          url: `${API_URL}/comment/`,
          })
          .then((res) => {
              CommentList.value = res.data
              console.log('전체댓글 조회')
          })
          .catch((err) => {
              console.log(err, '전체댓글 조회실패')
              CommentList.value = ''
          })
  }



  return {
    API_URL, User, Token, isLogin, signUp, logIn, logOut, getUser,
     stocks, saveproducts, depositsproducts, fundproducts, stockproducts, stockplusproducts,
      stockRecommend, stockplusRecommend, fundRecommend, saveRecommend, depositsRecommend, depositsAllproducts, savingAllproducts,
      profitData,assetData,getProfitData,getAssetData,
      getCommentList, CommentList,
    }
}, {
  persist: true
})