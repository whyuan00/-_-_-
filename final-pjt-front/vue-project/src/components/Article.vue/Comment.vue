<template>
    <div>

        <div v-if="comment">
            - <span > {{ comment.username }} </span> :
            <span > " {{ comment.content }} " </span>
            <span class="btn btn-light">
                <button v-if="comment.user == store.User.id" @click="deleteComment(comment.id)"> 삭제
                </button>
            </span>
            <hr />
        </div>
    </div>

</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watchEffect, watch } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
// const commentlist = ref([])

defineProps({
    comment: Object
})

const deleteComment = function(comment_id){
      axios({
        method:'delete',
        url: `${store.API_URL}/comment/detail/${comment_id}/`,
        headers: {
          Authorization: `Token ${store.Token}`
        }
      })
      .then((res)=>{
        store.getCommentList() // 전체 코멘트
        console.log('댓글삭제')
      })
      .catch((error)=>{
        console.log('댓글삭제 실패')
      })
  }


</script>


<style scoped>
.container {
    display: flex;
    flex-direction: column;
}

.postbox {
    height: 80%;
}

.commentform {
    height: 20%;
}

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