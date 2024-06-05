<template>
    <div class="text-center">
        <nav>
            <router-link :to="{ name: 'mypageview' }"> 내 정보</router-link> |
            <router-link :to="{ name: 'searchpageview' }"> 프로필 검색</router-link>
        </nav>
    </div>
    <div>
        <RouterView />
    </div>
</template>

<script setup>

</script>

<style scoped></style>
