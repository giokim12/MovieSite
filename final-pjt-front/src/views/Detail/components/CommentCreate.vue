<template>
  <div class="bg-[#1C1C1C] p-5 w-[650px]">
    <div class="text-3xl">{{ movie?.title }}</div>
    <div class="text-3xl">어떠셨나요?</div>
    <div class="text-xl my-3">다른 사용자가 참고할 수 있도록 리뷰를 남겨보세요.</div>
    <form @submit.prevent="createComment">
      <input type="submit" id="submit" class="float-right bg-[gray] p-2 mt-1 rounded" value="작성하기"/>
      <StarRatingVue v-model="rate"/>
      <span></span>
      <textarea v-model="content" name="content" id="content" cols="48" rows="10" class="text-white bg-black text-2xl mt-1"></textarea>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import StarRatingVue from './StarRating.vue'

export default {
  name: "CommentCreate",
  data() {
    return {
      rate: 3,
      content: null,
    }
  },
  props: {
    movie: Object,
  },
  components: {
    StarRatingVue
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  methods: {
    createComment() {
      if (!this.isLogin) {
        alert('로그인이 하세용.')
      } else if (this.isLogin){
        console.log(this.$store.state.userdata)
        const rate = this.rate
        const content = this.content
        if (!rate) {
          alert('평점.. 입력..')
          return
        } else if (!content) {
          alert('내용.. 입력..')
          return
        }
        axios({
          method: 'POST',
          url: `${API_URL}/api/v1/movies/${this.movie.movie_id}/comments/`,
          data: {
            // movie: this.movie.movie_id,
            rate: this.rate,
            content: this.content,
            user_id: this.$store.state.userdata.id
          },
          headers: {
            Authorization: `Bearer ${this.$store.state.access}`
          }
        })
          .then(() => {
            this.content = null
            this.rate = 3
            this.$store.dispatch({
              type: "getCommentList",
              movie_id: this.$route.params.movie_id, 
              sort: 'NEW'
            })
          })
          .catch((err) => {
            console.log('err = ', err)
          })
      }
    }
  }
}
</script>

<style>

</style>