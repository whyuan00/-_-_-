<template>
    <div>
        <div class = "fontstyle" style="display:flex;justify-content: space-evenly;">
            <RouterLink :to="{name:'profitdataview'}"> click! 수익 기준 ▼</RouterLink>
            |
            <RouterLink :to="{name:'assetdataview'}"> click! 총 자산 기준 ▼</RouterLink>
        </div>
        <div>
            <RouterView/>
        </div>
    </div>
</template>

<script setup>
</script>
    
<style  scoped>
.fontstyle {
    font-family: 'Noto Sans KR', sans-serif;
}

.title {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 100px;
    font-size: 30px;
    font-weight: bold;
    color: #333;
}
</style>