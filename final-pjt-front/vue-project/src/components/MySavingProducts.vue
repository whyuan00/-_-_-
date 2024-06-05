<template>
    <div>
        <div v-for="favSavingProduct in favSavingProducts" :key="favSavingProduct.id">
            <div v-for="product in favSavingProduct.product" :key="product.id">
                <div class="product-box-info">
                    <router-link :to="{ name: 'mysavingdetailview', params: { id: product.fin_prdt_cd } }">
                        <h4>{{ product.fin_prdt_nm }}</h4>
                    </router-link>
                    <p>{{ product.kor_co_nm }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { RouterLink } from 'vue-router' 

// props로 받은 favProducts 선언
const props = defineProps({
favSavingProducts: {
    type: Object,
    required: true,
}
})
</script>

<style scoped>
.subtitle {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: bold;
    margin-top: 50px;
    margin-bottom: 30px;
}

.product-box:hover {
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
}

.product-box-info {
    font-family: 'Noto Sans KR', sans-serif;
    color: #333;
    margin: 10px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    transition: box-shadow 0.3s ease;
}
</style>