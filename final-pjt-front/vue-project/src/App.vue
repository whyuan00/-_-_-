<template>
  <nav class="navbar navbar-expand-lg navbar-light text-toss-blue border-bottom fixed-top">
    <div class="container-fluid custom-container">
      <div class="d-flex align-items-center">
        <RouterLink class="navbar-brand text-toss-blue" :to="{ name: 'home' }">Home</RouterLink>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" ref="navbarToggler">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="navbarNav" ref="navbarCollapse">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <RouterLink   @click="closeNavbar"  class="nav-link text-toss-blue" :to="{ name: 'finlifeview' }">예적금 상품 알아보기
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'exchangerateview' }">환율 정보 알아보기
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'mapview' }">지도
              </RouterLink>
            </li>
            <li class="nav-item" v-if="LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'recommendview' }"> 분야 별 금융 상품 추천 </RouterLink>
            </li>
            <li class="nav-item" v-if="LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'gameview' }">나의 투자성향 확인하기 </RouterLink>
            </li>
            <li class="nav-item" v-if="LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'articleview' }"> 커뮤니티 </RouterLink>
            </li>
            <li class="nav-item" v-if="!LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'signupview' }"> 회원가입 </RouterLink>
            </li>
            <li class="nav-item" v-if="!LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'loginview' }">로그인</RouterLink>
            </li>
            <li class="nav-item" v-if="LogIn">
              <RouterLink   @click="closeNavbar" class="nav-link text-toss-blue" :to="{ name: 'logoutview' }">로그아웃</RouterLink>
            </li>
            <li class="nav-item" v-if="LogIn">
              <RouterLink  @click="closeNavbar"  class="nav-link text-toss-blue" :to="{ name: 'mypageview' }">Mypage</RouterLink>
            </li>
          </ul>
        </div>
      </div>
  </nav>

  <div class="container mt-4">
    <RouterView />
  </div>

</template>

<script setup>
import { computed,ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'

const navbarToggler = ref(null);
const navbarCollapse = ref(null);

const closeNavbar = function() {
  if (navbarCollapse.value.classList.contains("show")) {
    navbarToggler.value.click();
  }
}

const store = useCounterStore()
const LogIn = computed(() => {
  return store.isLogin 
})


</script>

<style scoped>
button {
  position: absolute;
  right:170px;
}

.text-toss-blue {
  color: #339af0 !important;
  text-align: right;
  background-color: white
}


body,
.navbar,
.nav-link,
.navbar-brand {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 400;
}

.navbar-brand,
.nav-link {
  font-weight: 500;
}

.nav-link:hover {
  background-color: rgba(51, 154, 240, 0.1);
  border-radius: 5px;
}

.navbar-toggler-icon {
  filter: invert(51%) sepia(84%) saturate(2211%) hue-rotate(184deg) brightness(101%) contrast(102%);
}

.custom-container {
  margin-left: 10rem;

  margin-right: 10rem;

}

.container {
  margin-top: 20px;
  background-color: white;
}
</style>
