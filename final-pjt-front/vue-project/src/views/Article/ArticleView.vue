<template>
    <div class="bigbox" style="margin: -80px;">
        <div class="ranking">
            <h3 class="title">현재, 나의 랭킹은?</h3>
            <p class="fontstyle">* 나의 투자성향 게임 결과를 바탕으로, 랭킹을 보여드립니다. </p>
            <hr>
            <div class="ranking">
                <Ranking />
            </div>
        </div>

        <div class="comunity">
            <h3 class="title">커뮤니티 게시판</h3>
            <p class="fontstyle">* 자유롭게 댓글을 달아주세요 ! 지나친 욕설이나 비방은 금지 ^^</p>
            <hr>
            <div class="container scroll ">
                <div class="postbox">
                    <Comment v-for="comment in store.CommentList" :comment="comment" />
                </div>
            </div>

            <div class="commentform">

                <h2>Leave a Comment</h2>
                <form @submit.prevent="submitComment" style="border-inline-color: black;">
                    <input style="border: 0.5px solid skyblue; padding:4px;" id="comment" type="text" v-model="content">
                    <button
                        style="border: 0.5px solid skyblue; padding:5px; border-radius: 5px; margin-left:20px; ; ">댓글
                        생성</button>
                </form>
            </div>
        </div>




    </div>
</template>


<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import Ranking from '@/components/Article.vue/Ranking.vue';
import Comment from '@/components/Article.vue/Comment.vue';

const content = ref(null)
const store = useCounterStore()

// 게시판 들어오면 항상 data update
onMounted(() => {
    store.getProfitData //전체 profit
    store.getAssetData() // 전체 asset
    store.getCommentList() // 전체 코멘트
})

const submitComment = function () {
    if (content.value.length > 18) {
        alert('20글자 이내로 작성해 주세요')
        content.value = ''
    }
    axios({
        method: 'post',
        url: `${store.API_URL}/comment/${store.User.id}/`,
        data: { content: content.value },
        headers: {
            Authorization: `Token ${store.Token}`
        }
    })
        .then((res) => {
            console.log('댓글생성')
            content.value = ''
            store.getCommentList() // 전체 코멘트
        })
        .catch((error) => {
            console.log('댓글생성 실패', error)
        })
}


</script>

<style scoped>
.bigbox {
    font-family: 'Noto Sans KR', sans-serif;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.ranking community {
    font-family: 'Noto Sans KR', sans-serif;
    display: flex;
    flex-direction: column;
}
.scroll {
    max-height: 300px; 
    overflow-y: auto;
}
.container {
    max-height: 300px; /* 최대 높이 설정 */
    overflow-y: auto; /* 내용이 컨테이너를 넘치면 스크롤 생성 */
}
.commentform {
    position: fixed;
    bottom: 230px;
    left: 75%;
    transform: translateX(-50%);
    width: 50%;
    max-width: 400px; 
    padding: 10px; 
    background-color: white; 
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
</style>