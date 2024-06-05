<template>
    <div>
        <h1>로그인</h1>
        <div class="box">
            <form @submit.prevent="logIn">
                <!-- Username input -->
                <div data-mdb-input-init class="form-outline mb-4">
                    <input type="text" id="username" class="form-control" v-model.trim="username" autocomplete="username"/>
                    <label class="form-label" for="username">Username</label>
                </div>

                <!-- Password input -->
                <div data-mdb-input-init class="form-outline mb-4">
                    <input type="password" id="password" class="form-control" v-model.trim="password" autocomplete="current-password" />
                    <label class="form-label" for="password">Password</label>
                </div>

                <input data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-3" type="submit" value="로그인">
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value,
    }
    store.logIn(payload)
}

</script>

<style scoped>
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
    border: 2px solid rgb(226, 223, 223);
    border-radius: 10px;
    box-sizing: border-box;
}

.box > * {
    width: 100%;
}
</style>