<template>
    <div class="m-3" @click="goDetail(movie.id)">
      <img class="w-64 h-80" :src="imgPath" alt="...">
    </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie.poster_path
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({name: 'detail', params: {id}})
    }
  }
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