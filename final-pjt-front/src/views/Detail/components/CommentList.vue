<template>
  <div>
    <div>나는 댓글리스트</div>
    <CommentListItemVue
      v-for="(comment, idx) in get_comment"
      :key="idx"
      :comment="comment"
    />
  </div>
  
</template>

<script>
import CommentListItemVue from './CommentListItem.vue'
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "CommentList",
  components: {
    CommentListItemVue,
  },
  props: {
    movie: Object,
  },
  computed: {
    get_comment () {
      return this.$store.state.comments
    }
  },
  created() {
    this.getCommentList()
  },
  methods: {
    getCommentList() {
      this.$store.dispatch("getCommentList", this.$route.params.movie_id)
    }
  }
}
</script>

<style>

</style>