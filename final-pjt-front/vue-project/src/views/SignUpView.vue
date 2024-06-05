<template>
  <div>
      <h1 class="fontstyle">회원 가입</h1>
      <div class="signupbox">
          <form @submit.prevent="signUp">
              <!-- Username input -->
              <div data-mdb-input-init class="form-outline mb-4">
                  <input type="text" id="username" class="form-control" v-model.trim="username" />
                  <label class="form-label" for="username">Username</label>
              </div>

              <!-- Email input -->
              <div data-mdb-input-init class="form-outline mb-4">
                  <input type="email" id="email" class="form-control" />
                  <label class="form-label" for="email">Email</label>
              </div>

              <!-- Password input -->
              <div data-mdb-input-init class="form-outline mb-4">
                  <input type="password" id="password1" class="form-control" v-model.trim="password1" />
                  <label class="form-label" for="password1">Password</label>
              </div>

              <!-- Repeat Password input -->
              <div data-mdb-input-init class="form-outline mb-4">
                  <input type="password" id="password2"  class="form-control" v-model.trim="password2"  />
                  <label class="form-label" for="password2">Repeat password</label>
              </div>
              <input data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-3" type="submit" value="회원가입">
          </form>
      </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'
import axios from 'axios'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/accounts/signup/`,
      data: {
        username:username.value,
        password1:password1.value,
        password2:password2.value,
      }
    })
      .then(res => {
        console.log('회원가입완료')
        const password = password1
        store.logIn({ username:username.value, password:password1.value })
      })
      .catch(error => {
        console.log('회원가입실패',error)
        alert('이미 존재하는 아이디 입니다. 다시 시도해 주세요')
      })
  }

</script>

<style scoped>
h1 {
  font-family: 'Noto Sans KR', sans-serif;
  text-align: center;
}

.signupbox {
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 90%; 
  max-width: 600px;
  margin: 0 auto; 
  padding: 20px;
  border: 2px solid rgb(226, 223, 223); 
  border-radius: 10px;
  box-sizing: border-box; 
}

.signupbox > * {
  font-family: 'Noto Sans KR', sans-serif;
  width: 100%;
}

.fontstyle {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 400px;
}

</style>
<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">
