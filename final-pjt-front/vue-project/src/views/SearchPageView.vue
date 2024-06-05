<template>
    <router-link to="/" class="btn btn-secondary mt-3">뒤로가기</router-link>
    <br>
    <br>
    <div class="container">
        <div class="mt-3">

            <p>다른 사람의 프로필도 검색해 보세요</p>
            <div class="input-group mb-3">
                <input v-model="newname" type="text" class="form-control" placeholder="사용자 이름을 입력하세요">
                <button @click="search" class="btn btn-primary">검색</button>
            </div>
        </div>

        <div class="mt-5" v-if="user" style="border: 1px solid #ccc; border-radius: 5px; padding: 10px;">
            <h1>{{ user.username }} 정보</h1>
            <p v-show="user.myproduts">
                상품 목록 {{ user.myproduts }}
            </p>
        </div>

        <div class="mt-5" v-if="searched && !user">
            <h2>검색 결과가 없습니다</h2>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
const newname = ref(null)
const user = ref(null)
const searched = ref(false)

const search = function () {
    store.getUser(newname.value)
        .then((response) => {
            user.value = response
            console.log(`${user.value.username} 정보 확인`)
            searched.value = false
        })
        .catch((error) => {
            console.error('사용자 정보 가져오기 실패', error)
            user.value = null
            searched.value = true
        })
}
</script>

<style scoped>
.container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
}

.input-group {
    display: flex;
}

.form-control {
    flex: 1;
}

.btn {
    margin-left: 10px;
}

@media (max-width: 767px) {
    .container {
        padding: 0 10px;
    }
}
</style>