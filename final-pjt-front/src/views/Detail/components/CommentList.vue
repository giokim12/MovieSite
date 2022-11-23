<template>
  <div>
    <select id="sort" v-model="sortKey" @change="getCommentList" class="bg-black text-white h-16 text-xl rounded-lg border-none focus:outline-none">
      <option value="NEW">최신순</option>
      <option value="RATE_UP">평점 높은순</option>
      <option value="RATE_DOWN">평점 낮은순</option>
      <option value="LIKES">좋아요순</option>
    </select>
    <CommentListItemVue
      v-for="(comment, idx) in get_comment"
      :key="idx"
      :comment="comment"
      v-on:del="getCommentList"
      v-on:like="getCommentList"
    />
  </div>
</template>

<script>
import CommentListItemVue from './CommentListItem.vue'
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "CommentList",
  data() {
    return {
      selectArrow: false,
      sortKey: 'NEW'
    }
  },
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
      this.$store.dispatch({
        type: "getCommentList",
        movie_id: this.$route.params.movie_id, 
        sort: this.sortKey
      })
      // this.$refs.CommentListItemVue.getCommentLike()
    }
    // onChange(e) {
    //   console.log(e.target.value)
    // }
  }
}
</script>

<style>

</style>