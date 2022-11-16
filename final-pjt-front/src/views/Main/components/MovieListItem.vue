<template>
  <div>
    <div>{{ movie }}</div>
    <div class="max-w-sm rounded overflow-hidden shadow-lg" @click="goDetail(movie.id)">
      <img class="w-full" :src="imgPath" alt="...">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">{{ movie.title }}</div>
        <p class="text-gray-700 text-base overview">
          {{ movie.overview }}
        </p>
      </div>
      <div class="px-6 pt-4 pb-2">
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{{ }}</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
      </div>
    </div>
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