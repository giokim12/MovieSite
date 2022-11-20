<template>
  <div>
    <h2>나는 댓글다는곳</h2>
    <form @submit.prevent="createComment">
      <label for="rate">별점</label>
      <!-- <input v-model="rate" type="number" id="rate"> -->
      <StarRatingVue v-model="rate"/>
      <textarea v-model="content" name="content" id="content" cols="30" rows="10"></textarea>
      <br>
      <input type="submit" id="submit" value="댓글 작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import StarRatingVue from './StarRating.vue'

export default {
  name: "CommentForm",
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
        alert('로그인이 필요합니다.')
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
          .then((res) => {
            console.log(res)
            this.$store.dispatch("getCommentList", this.$route.params.movie_id)
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