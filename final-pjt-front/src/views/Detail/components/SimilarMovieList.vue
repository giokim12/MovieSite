<template>
  <div class="flex">
    <hr>
    <h2 class="text-white">같은장르 영화</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_similar"
        :key = "idx"
        :movie = "movie"
      />
    </div>
  </div>

</template>

<script>
import MovieListItem from '@/views/Main/components/MovieListItem'
export default {
  name: "SimilarMovieList",
  components: {
    MovieListItem,
  },
  computed: {
    movies_similar() {
      return this.$store.state.moviesSimilar
    }
  }
}
</script>

<style>

</style>