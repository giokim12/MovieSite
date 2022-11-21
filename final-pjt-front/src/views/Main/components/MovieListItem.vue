<template>
    <div class="m-3 h-[100%]" @click="goDetail(), addView()">
      <img class="w-[90%] h-[100%] rounded-xl lg:hover:scale-110 lg:hover:rounded transition-transform ease-in-out duration-500 hover:cursor-pointer" :src="imgPath" alt="...">
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie.poster_path
    },
    isLogin() {
      return this.$store.state.access
    }
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'detail', params: { movie_id:this.movie.movie_id }})
    },
    addView() {
      if (this.isLogin) {
        axios ({
          method: 'POST',
          url: `${API_URL}/api/v1/detail/${this.movie.movie_id}/`,
          data: {
            user: this.$store.state.userdata.id,
            movie: this.movie.movie_id
          }
        })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
  },
}
</script>

<style>
.overview {
  display:-webkit-box; 
  word-wrap:break-word; 
  -webkit-line-clamp:4; 
  -webkit-box-orient:vertical; 
  overflow:hidden; 
  text-overflow:ellipsis;
}
</style>