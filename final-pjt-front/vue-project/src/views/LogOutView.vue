<template>
    <div>
    <h1>로그아웃 하시겠습니까? </h1>
     <button @click="useCounterStore().logOut"> 로그아웃 </button>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter.js'
</script>

<style  scoped>

</style>